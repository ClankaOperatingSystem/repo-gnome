"""Check every file of the gnome against the formats its consumers
read, before a pull request is opened: the doctrine, the policies, the
manifest and the cases, in the terms bugflow's docs/policy-package.md
gives. The three checks in the skill's scripts/ are run over their own
cases, and must report each seeded case and no clean one. The skill's
copy of the doctrine and the policies must be what tools/compile.py
writes.
"""

import filecmp
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from compile import compile_skills  # noqa: E402

SKILL = ROOT / "skills" / "repo-gnome-tidy"
SCRIPTS = SKILL / "scripts"
POLICIES = sorted((ROOT / "policies").glob("*.md"))
DOCTRINE = sorted((ROOT / "doctrine").glob("*.md"))
CASES = sorted((ROOT / "cases").glob("*/*.md"))

POLICY_REQUIRED = (
    "policy_id",
    "subject",
    "summary",
    "model_class",
    "evidence",
    "quotable_name",
    "graded",
    "quotes_code",
)
POLICY_OPTIONAL = ("ceiling", "implemented")
MODEL_CLASSES = ("none", "small", "medium", "large")
SUBJECTS = ("document/file", "scope/canon")
GRADES = ("warn", "fail")
CASE_LINES = ("title", "expect", "grade", "why", "path")
CLAUSE = re.compile(r"\*\*([A-Z]+-\d+)\. (.+?)\.\*\*")
CASE_NAME = re.compile(r"^(clean|seeded)-(\d\d)-[a-z0-9-]+\.md$")
ID = re.compile(r"^[A-Z]+-\d+$")


def header_of(text: str) -> tuple[list[tuple[str, str]], str]:
    """The header's key-value lines in order, and the text after the
    three dashes."""
    header, separator, rest = text.partition("\n---\n")
    assert separator, "no --- line after the header"
    lines = []
    for line in header.split("\n"):
        key, colon, value = line.partition(":")
        assert colon, f"header line {line!r} is not key: value"
        lines.append((key, value.strip()))
    return lines, rest


def policy_of(path: Path) -> dict:
    lines, rest = header_of(path.read_text())
    policy: dict = {"path": path, "clauses": {}}
    for key, value in lines:
        if key == "clause":
            clause_id, _, name = value.partition(" ")
            policy["clauses"][clause_id] = name
        else:
            assert key not in policy, f"{path.name}: two {key} lines"
            policy[key] = value
    instructions, separator, notes = rest.partition("\n=== calibration\n")
    policy["instructions"] = instructions
    policy["notes"] = notes if separator else None
    return policy


def case_of(path: Path) -> dict:
    lines, rest = header_of(path.read_text())
    case: dict = {"file": path, "policy": path.parent.name, "body": rest}
    for key, value in lines:
        assert key not in case, f"{path}: two {key} lines"
        case[key] = value
    return case


def manifest_of() -> dict:
    lines, _ = header_of((ROOT / "manifest.md").read_text())
    fields = dict(lines)
    return {
        "agent_id": fields["agent_id"],
        "subjects": [one.strip() for one in fields["subjects"].split(",")],
        "policies": [one.strip() for one in fields["policies"].split(",")],
    }


DOCTRINE_TEXT = "\n\n".join(path.read_text() for path in DOCTRINE)
CLAUSES = CLAUSE.findall(DOCTRINE_TEXT)
CLAUSE_IDS = {clause_id for clause_id, _ in CLAUSES}
POLICY_BY_ID = {policy_of(path)["policy_id"]: policy_of(path) for path in POLICIES}
MANIFEST = manifest_of()


# The doctrine


def test_each_clause_id_is_used_once() -> None:
    seen = [clause_id for clause_id, _ in CLAUSES]
    assert len(seen) == len(set(seen)), sorted(
        one for one in seen if seen.count(one) > 1
    )


def test_the_preamble_comes_first() -> None:
    assert DOCTRINE[0].name == "00-preamble.md"


# The policies


@pytest.mark.parametrize("path", POLICIES, ids=lambda p: p.name)
def test_the_policy_header_holds_the_lines_the_consumers_read(path: Path) -> None:
    policy = policy_of(path)
    keys = {
        key
        for key in policy
        if key not in ("path", "clauses", "instructions", "notes")
    }
    assert set(POLICY_REQUIRED) <= keys, f"missing {set(POLICY_REQUIRED) - keys}"
    assert keys <= set(POLICY_REQUIRED) | set(POLICY_OPTIONAL), (
        f"unknown {keys - set(POLICY_REQUIRED) - set(POLICY_OPTIONAL)}"
    )
    assert policy["model_class"] in MODEL_CLASSES
    assert policy["evidence"] in SUBJECTS
    assert policy["graded"] in ("yes", "no")
    assert policy["quotes_code"] in ("yes", "no")
    assert policy.get("ceiling", "fail") in GRADES
    assert policy.get("implemented", "judge") in ("judge", "check")
    assert policy["clauses"], "no clause line"
    assert policy["notes"] is not None, "no === calibration line"


@pytest.mark.parametrize("path", POLICIES, ids=lambda p: p.name)
def test_the_policy_id_opens_its_filename(path: Path) -> None:
    policy = policy_of(path)
    assert ID.match(policy["policy_id"])
    assert path.name.startswith(policy["policy_id"] + "-")


@pytest.mark.parametrize("path", POLICIES, ids=lambda p: p.name)
def test_the_policy_lists_clauses_the_doctrine_has(path: Path) -> None:
    policy = policy_of(path)
    for clause_id, name in policy["clauses"].items():
        assert clause_id in CLAUSE_IDS, f"{clause_id} is not a clause"
        assert name, f"{clause_id} has no name"


@pytest.mark.parametrize("path", POLICIES, ids=lambda p: p.name)
def test_a_checked_policy_names_no_model_and_a_judged_one_does(path: Path) -> None:
    policy = policy_of(path)
    if policy.get("implemented", "judge") == "check":
        assert policy["model_class"] == "none"
        assert policy["evidence"] in MANIFEST["subjects"]
    else:
        assert policy["model_class"] != "none"


def test_the_policy_ids_are_distinct() -> None:
    ids = [policy_of(path)["policy_id"] for path in POLICIES]
    assert len(ids) == len(set(ids))


# The manifest and the scripts


def test_the_manifest_lists_every_policy_once() -> None:
    assert sorted(MANIFEST["policies"]) == sorted(POLICY_BY_ID)
    assert len(MANIFEST["policies"]) == len(set(MANIFEST["policies"]))


def test_the_manifest_subjects_cover_the_policies() -> None:
    for policy in POLICY_BY_ID.values():
        assert policy["evidence"] in MANIFEST["subjects"]


def checked_policies() -> dict[str, str]:
    """Each checked policy's id and the command its instructions name."""
    named = {}
    for policy_id, policy in POLICY_BY_ID.items():
        if policy.get("implemented") != "check":
            continue
        found = re.search(
            r"check `(check-[a-z-]+)` in `scripts/`", policy["instructions"]
        )
        assert found, f"{policy_id} names no command"
        named[policy_id] = found.group(1)
    return named


def test_each_checked_policy_names_a_script_that_exists() -> None:
    for policy_id, command in checked_policies().items():
        assert (SCRIPTS / command).is_file(), f"no scripts/{command}"


def test_each_check_script_answers_a_checked_policy() -> None:
    scripts = [path.name for path in SCRIPTS.glob("check-*")]
    assert sorted(scripts) == sorted(checked_policies().values())


def test_every_skill_carries_the_methodologys_prefix() -> None:
    for skill in (ROOT / "skills").iterdir():
        assert skill.name.startswith("repo-gnome-"), skill.name
        assert (skill / "SKILL.md").is_file()


def test_each_skill_holds_what_compile_writes() -> None:
    with tempfile.TemporaryDirectory() as scratch:
        for written in compile_skills(Path(scratch)):
            name = written.parent.name
            committed = ROOT / "skills" / name / "references"
            assert committed.is_dir(), f"{name}: run make skills"
            assert_same_tree(written, committed)


def assert_same_tree(left: Path, right: Path) -> None:
    compared = filecmp.dircmp(left, right)
    assert not compared.left_only, f"{right}: missing {compared.left_only}; run make skills"
    assert not compared.right_only, f"{right}: extra {compared.right_only}; run make skills"
    _, mismatch, errors = filecmp.cmpfiles(
        left, right, compared.common_files, shallow=False
    )
    assert not mismatch and not errors, f"{right}: differs in {mismatch}; run make skills"
    for name in compared.common_dirs:
        assert_same_tree(left / name, right / name)


# The cases


@pytest.mark.parametrize("path", CASES, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_the_case_is_named_and_shaped_as_a_case(path: Path) -> None:
    assert CASE_NAME.match(path.name), path.name
    case = case_of(path)
    assert case["policy"] in POLICY_BY_ID, f"no policy {case['policy']}"
    for key in case:
        if key in ("file", "policy", "body"):
            continue
        assert key in CASE_LINES, f"unknown line {key}"
    assert case["title"]
    assert case["why"]
    assert case["body"].strip()
    policy = POLICY_BY_ID[case["policy"]]
    if path.name.startswith("clean-"):
        assert case["expect"] == ""
        assert "grade" not in case
    else:
        assert case["expect"] in policy["clauses"], (
            f"{case['expect']} is not a clause {case['policy']} judges"
        )
        assert case["grade"] in GRADES
        if policy.get("ceiling") == "warn":
            assert case["grade"] == "warn"


def test_each_policy_has_a_seeded_case_and_a_clean_case() -> None:
    for policy_id in POLICY_BY_ID:
        names = [path.name for path in (ROOT / "cases" / policy_id).glob("*.md")]
        assert any(name.startswith("seeded-") for name in names), policy_id
        assert any(name.startswith("clean-") for name in names), policy_id


# The checks, run over their own cases


CHECKED = [
    (command, policy_id, next(iter(POLICY_BY_ID[policy_id]["clauses"])))
    for policy_id, command in checked_policies().items()
]


@pytest.mark.parametrize(
    "case",
    [path for path in CASES if path.parent.name in {w[1] for w in CHECKED}],
    ids=lambda p: f"{p.parent.name}/{p.name}",
)
def test_the_check_answers_its_case(case: Path) -> None:
    command, policy_id, clause = next(
        words for words in CHECKED if words[1] == case.parent.name
    )
    parsed = case_of(case)
    with tempfile.TemporaryDirectory() as scratch:
        target = Path(scratch) / parsed.get("path") if parsed.get("path") else Path(scratch) / "document.org"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(parsed["body"])
        run = subprocess.run(
            [str(SCRIPTS / command)],
            cwd=scratch,
            capture_output=True,
            text=True,
            check=False,
        )
    findings = [line for line in run.stdout.splitlines() if line]
    if case.name.startswith("clean-"):
        assert run.returncode == 0 and not findings, run.stdout
    else:
        assert run.returncode == 1, run.stdout + run.stderr
        assert findings, "no finding"
        assert all(clause in line for line in findings), run.stdout
        assert all(re.match(r"^\S+:\d+: ", line) for line in findings), run.stdout
