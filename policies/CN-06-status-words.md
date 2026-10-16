policy_id: CN-06
subject: canon
summary: Canon says what a thing is; where work stands is a task
model_class: none
evidence: document/file
quotable_name: document
graded: yes
quotes_code: no
ceiling: warn
implemented: check
clause: CANON-7 status in canon
---
Answered by the check `check-status-words` in `scripts/`, which reports a
line of prose holding one of these, under CANON-7, graded warn: "not yet",
"planned:", "none yet", "is not built", "has been used once", "remains to
be", "await", "awaits", "untested", "never run", "for now", "interim",
"work in progress". It also reports a heading named "Open questions",
"Gaps", "Known limitations" or "Status".

A line inside a task, that is, under a heading with a TODO keyword, is not
reported: tasks hold status. A line in a code block is not reported.
=== calibration
Not measured.
