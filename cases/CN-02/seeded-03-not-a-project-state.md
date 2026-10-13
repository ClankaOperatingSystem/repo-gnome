title: A skill that denies a state
expect: CANON-3
grade: warn
why: "BACKLOG is not a project state" denies a value after the three states are listed.
path: skills/project-handling/SKILL.md
---
# Project handling

The project's own Org file is the one authority for its state: give it a
`STATUS` property, `COMMITTED` before work starts, `WIP` once it has,
`DONE` when finished. `BACKLOG` is not a project state. Do not infer a
delivery commitment from the presence of extensive design notes.
