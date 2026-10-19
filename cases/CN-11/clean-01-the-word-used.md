title: A README that uses a word without defining it
expect:
why: The README installs a gnome and says nothing of what a gnome is.
path: README.md
---
=== document README.md
# pr-gnome

Install the gnome in your garden by declaring it as a methodology.
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
