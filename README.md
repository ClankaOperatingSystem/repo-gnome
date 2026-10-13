# The canon doctrine

Standards for canon: the documents a repository maintains and reads to do
its work. A doctrine of clauses, a policy for each judgement, cases that
test the judge, three checks that need no model, and a skill that applies
them.

This repository is a gnome: it implements the gnome protocol, which
bugflow's `docs/policy-package.md` specifies.

Two things read this repository and nothing in it is written for one
alone:

- **A garden node** declares it as a methodology, beneath its
  methodologies path, at a directory named `canon`:

      children:
        - path: methodologies/canon
          remote: git@github.com:ClankaOperatingSystem/canon-doctrine.git

  The node's tree tool links `skills/canon-tidy` into its skills and the
  checks in `bin/` into its commands, and its lint runs the checks that
  `methodology.yaml` names. poslib's `doc/pos-methodology.txt` says how.

- **A bugflow server** judges pull requests by it when a binding
  repository deploys it, with `declarations.toml` saying which
  repositories it applies to.

## What is here

| Path | What it is |
|---|---|
| `doctrine/*.md` | The doctrine, read in filename order as one document |
| `policies/CN-*.md` | One policy each: header, instructions, calibration notes |
| `cases/CN-*/*.md` | The cases of each policy: a document and the answer a correct judge gives |
| `manifest.md` | The gnome's id, subjects and policies |
| `bin/canon-*` | The checks: commands that answer three policies without a model |
| `lib/` | What the checks share |
| `skills/canon-tidy/` | The skill that applies the doctrine to a scope |
| `methodology.yaml` | The declaration a garden's lint reads: the checks to run |
| `tests/` | The checks that every file is in the format the consumers read |

## Words

- Doctrine: the standard, in `doctrine/`, joined in filename order.
- Clause: one rule of the doctrine, with an id such as `CANON-3`. An id is
  never reused.
- Policy: one question asked about a document, and the clauses it judges.
  A policy whose header says `implemented: check` is answered by the
  command its instructions name, in `bin/`, not by a model.
- Subject: the evidence a policy reads. `document/file` is one document;
  `scope/canon` is every document of a scope, which a pull request judge
  does not render.
- Case: an example document with the answer a correct judge gives it. A
  `clean` case expects nothing; a `seeded` case expects one clause.
- Finding: one thing a judge or a check reports, quoting the words at
  fault and citing a clause, graded `warn` or `fail`.

## The format of a case

A header, a line of three dashes, and the document:

    title: An entrance that dates a decision
    expect: CANON-2
    grade: warn
    why: The sentence names the decider and the date beside the rule.
    path: foss/index.org
    ---
    #+TITLE: FOSS
    ...

`path` is the document's path in its repository, which the subject
`document/file` renders. A clean case has an empty `expect` and no
`grade`. The `why` line is for a person; the judge is not shown it.

## Checks

    uv run --with pytest pytest -q

checks every file against the formats. The three commands in `bin/` run
in any directory, read its Org and Markdown files, and print findings as
`FILE:LINE: MESSAGE`, exit 1 when there are any.
