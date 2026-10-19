title: A guide that defines a check against its home
expect: CANON-12
grade: fail
why: The guide says a check is a test run by the server, which contradicts bugflow's line, where a check is a script in a skill.
path: docs/guide.md
---
=== document docs/guide.md
# Writing policies

A check is a test that the server runs on every commit before any
policy is judged.
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
