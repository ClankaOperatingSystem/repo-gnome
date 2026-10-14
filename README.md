# The canon doctrine

Standards for canon: the documents a repository maintains and reads to do
its work. A doctrine of clauses, a policy for each judgement, cases that
test the judge, three checks that need no model, and a skill that applies
them.

This repository is a gnome: it implements the gnome protocol, which
bugflow's [policy package](https://github.com/bugflow/bugflow/blob/master/docs/policy-package.md) specifies.
[What a gnome is](https://github.com/bugflow/bugflow/blob/master/docs/gnomes.md) explains a gnome's parts, who reads each,
and a maintainer's tasks.

Two things read this repository and nothing in it is written for one
alone:

- **A garden** declares it as a methodology in its configuration, at a
  tag:

      methodologies:
        - source: git@github.com:ClankaOperatingSystem/canon-doctrine.git
          ref: TAG

  The skills command-line tool copies `skills/canon-tidy/` into the
  garden's skills, and the garden's lint runs the checks in its
  `scripts/`.

- **A bugflow server** judges pull requests by it when a binding
  repository deploys it, with `declarations.toml` saying which
  repositories it applies to.

## What is here

| Path | What it is |
|---|---|
| `skills/canon-tidy/` | The skill that applies the doctrine to a scope |
| `skills/canon-tidy/references/doctrine/*.md` | The doctrine, read in filename order as one document |
| `skills/canon-tidy/references/policies/CN-*.md` | One policy each: header, instructions, calibration notes |
| `skills/canon-tidy/scripts/check-*` | The checks: scripts that answer three policies without a model |
| `skills/canon-tidy/scripts/lib/` | What the checks share |
| `cases/CN-*/*.md` | The cases of each policy: a document and the answer a correct judge gives |
| `manifest.md` | The gnome's id, subjects and policies |
| `tests/` | The checks that every file is in the format the consumers read |

The doctrine, the policies and the checks are inside the skill's
directory because the skills command-line tool copies a skill's
directory and nothing outside it.

## Words

- Doctrine: the standard, in `references/doctrine/`, joined in filename
  order.
- Clause: one rule of the doctrine, with an id such as `CANON-3`. An id is
  never reused.
- Policy: one question asked about a document, and the clauses it judges.
  A policy whose header says `implemented: check` is answered by the
  script its instructions name, in `scripts/`, not by a model.
- Subject: the evidence a policy reads. `document/file` is one document;
  `scope/canon` is every document of a scope, which a pull request judge
  does not render.
- Case: an example document with the answer a correct judge gives it. A
  `clean` case expects nothing; a `seeded` case expects one clause.
- Finding: one thing a judge or a check reports, quoting the words at
  fault and citing a clause, graded `warn` or `fail`.

## The formats

The [policy package](https://github.com/bugflow/bugflow/blob/master/docs/policy-package.md) specifies the manifest, a policy file
and a case. The tests here check every file against it.

## Checks

    uv run --with pytest pytest -q

checks every file against the formats. The three scripts in `scripts/`
run in any directory, read its Org and Markdown files, and print
findings as `FILE:LINE: MESSAGE`, exit 1 when there are any.
