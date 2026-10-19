title: A README that links to a word's home
expect:
why: One sentence names where the word is defined and links to it.
path: README.md
---
=== document README.md
# pr-gnome

What a gnome is, is in [bugflow's words](https://github.com/bugflow/bugflow/blob/master/docs/words.md).
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
