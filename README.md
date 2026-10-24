# repo-gnome

Standards for canon: the documents a repository maintains and reads to do
its work. This repository holds a doctrine of clauses, a policy for each
judgement, cases that test the judge, three checks that need no model, and
a skill that applies them.

This repository is a gnome: a methodology that also holds a doctrine,
its policies and its cases. bugflow's
[What a gnome is](https://github.com/bugflow/bugflow/blob/master/docs/gnomes.md)
defines a gnome and a maintainer's tasks, its
[policy package](https://github.com/bugflow/bugflow/blob/master/docs/policy-package.md)
specifies each file, and its
[words](https://github.com/bugflow/bugflow/blob/master/docs/words.md)
give each term one line.

Two things read this repository and nothing in it is written for one
alone:

- **A garden** declares it as a methodology in its configuration, at a
  tag, as ClankOS's `clankos-run help install` says:

      methodologies:
        - source: https://github.com/ClankaOperatingSystem/repo-gnome.git
          ref: TAG

  The skills command-line tool copies `skills/repo-gnome-tidy/` into the
  garden's skills, and the garden's lint runs the checks in its
  `scripts/`.

- **A bugflow server** judges pull requests by it when a binding
  deploys it. bugflow's
  [review document](https://github.com/bugflow/bugflow/blob/master/docs/review.md)
  says what a review writes and where each part comes from.

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

`doctrine/` and `policies/` are the originals. After a change in
either, run `make skills`, which writes the skill's copy in its
`references/`; the tests fail if the copy is out of date.

## Checks

    uv run --with pytest pytest -q

checks every file against the formats. The three scripts in `scripts/`
run in any directory, read its Org and Markdown files, and print
findings as `FILE:LINE: MESSAGE`, exit 1 when there are any.

## Website

The standards are published at
<https://clankaoperatingsystem.github.io/repo-gnome/>. The site renders
the standards, with a worked example from the cases and the commands
that check a document. The text the site adds, its introduction, its
scope and the example, is in `site.toml`.

`requirements-site.txt` pins the renderer release and its wheel
checksum. To build the site, install that file and run this from a
clean checkout:

```sh
python -m pip install -r requirements-site.txt
gnome-site . _site --title repo-gnome \
  --repository https://github.com/ClankaOperatingSystem/repo-gnome \
  --revision "$(git rev-parse HEAD)" --content site.toml
```

The output directory must be new or empty. The Website workflow runs
the tests and builds a `repo-gnome-site` artifact for each pull
request, which is downloaded and opened at `index.html` to see the
change. A change merged to `master` replaces the published site once
the tests pass. Source links on the site name the commit it was
rendered from, and the addresses of policies and the anchors of
clauses stay the same from one render to the next.

## Licence

This repository is free software under the GNU General Public License,
version 3 or any later version. The text is in `COPYING`.
