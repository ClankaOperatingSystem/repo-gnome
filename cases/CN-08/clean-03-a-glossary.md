title: A glossary of the repository's words
expect:
why: The entries are terms, each defined once, and no entry records an event.
path: README.md
---
# Review policies

## Words

Each thing has one word here, and the files use the same one.

- Gnome: `rules/`, fetched at one commit from the repository that
  `gnomes.toml` names.
- Doctrine: the files of `rules/references/doctrine/`, read in filename
  order as one document.
- Clause: one rule of the doctrine. It has an id, such as `VOICE-6`, and
  a name, such as "Marketing register".
- Policy: one question that a model is asked about a pull request, and
  the clauses that the question judges.
- Case: an example pull request, stored with the answer that a correct
  judge gives it.
