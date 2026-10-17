# repo-gnome

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
        - source: https://github.com/ClankaOperatingSystem/repo-gnome.git
          ref: TAG

  The skills command-line tool copies `skills/repo-gnome-tidy/` into the
  garden's skills, and the garden's lint runs the checks in its
  `scripts/`.

- **A bugflow server** judges pull requests by it when a binding
  repository deploys it, with `declarations.toml` saying which
  repositories it applies to.

## What is here

| Path | What it is |
|---|---|
| `doctrine/*.md` | The doctrine, read in filename order as one document |
| `policies/CN-*.md` | One policy each: header, instructions, calibration notes |
| `skills/repo-gnome-tidy/` | The skill that applies the doctrine to a scope |
| `skills/repo-gnome-tidy/references/` | A copy of `doctrine/` and `policies/`, written by `make skills` |
| `skills/repo-gnome-tidy/scripts/check-*` | The checks: scripts that answer three policies without a model |
| `skills/repo-gnome-tidy/scripts/lib/` | What the checks share |
| `cases/CN-*/*.md` | The cases of each policy: a document and the answer a correct judge gives |
| `manifest.md` | The gnome's id, subjects and policies |
| `tools/compile.py` | What `make skills` runs |
| `tests/` | The checks that every file is in the format the consumers read |

The doctrine and the policies are kept in `doctrine/` and `policies/`.
The skills command-line tool copies a skill's directory and nothing
outside it, so the skill carries a copy of both in its `references/`.
After a change in `doctrine/` or `policies/`, run `make skills`. The
tests fail if the copy is out of date.

## Words

- Doctrine: the standard, in `doctrine/`, joined in filename order.
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

## Website

[Read the current standards](https://clankaoperatingsystem.github.io/repo-gnome/).
The site includes worked examples and paths for contributors, maintainers and
people assessing the standards. Its reader guidance is in `site.toml`.

`requirements-site.txt` pins the renderer release and its wheel checksum.
To build locally, install that file and run this from a clean checkout:

```sh
python -m pip install -r requirements-site.txt
gnome-site . _site --title repo-gnome \
  --repository https://github.com/ClankaOperatingSystem/repo-gnome \
  --revision "$(git rev-parse HEAD)" --content site.toml
```

The output directory must be new or empty. The Website workflow runs the source
checks and builds a downloadable `repo-gnome-site` artifact for each pull request.
Download and extract that artifact, then open `index.html` to review it.
Changes on `master` replace the current GitHub Pages site after the checks pass.
The repository's Pages publishing source is GitHub Actions.

The gnome's maintainers own `site.toml`, the renderer pin and the workflow.
Review the preview when changing standards or upgrading the renderer. Source
links identify the rendered commit; policy routes and clause anchors stay stable.

## Licence

This repository is free software under the GNU General Public License,
version 3 or any later version. The text is in `COPYING`.
