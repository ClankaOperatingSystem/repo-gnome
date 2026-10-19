title: A README that defines a gnome as bugflow does
expect: CANON-12
grade: warn
why: The README says what a gnome is, in words that agree with bugflow's, the word's owner.
path: README.md
---
=== document README.md
# pr-gnome

A gnome is a repository that holds an editorial standard for one kind
of thing and the means to keep to it. This one is for pull requests.
=== glossary glossary/bugflow/docs/words.md
- **Gnome.** A repository that holds an editorial standard for one
  kind of thing and the means to keep to it. [What a gnome is](gnomes.md).
- **Check.** A script in a skill's `scripts/`, `check-<name>`, that
  answers a policy in code. [What a gnome is](gnomes.md).
- **Skill.** ClankOS's word, in its
  [words](https://github.com/ClankaOperatingSystem/clankos/blob/master/docs/words.txt).
=== glossary glossary/clankos/docs/words.txt
    skill             a folder holding SKILL.md in the agentskills.io
                      format ("clankos-run help model", 1)
    gnome             bugflow's word, in its docs/words.md
    check             bugflow's word, in its docs/words.md
