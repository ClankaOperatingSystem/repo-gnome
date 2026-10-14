policy_id: CN-01
subject: canon
summary: A rule is stated without who decided it or when
model_class: none
evidence: document/file
quotable_name: document
graded: yes
quotes_code: no
ceiling: warn
implemented: check
clause: CANON-2 dated ruling
---
Answered by the check `check-dated-ruling` in `scripts/`, which reports a
sentence that names a decision and a date together: a form of "ruled",
"decided", "agreed", "accepted" or "approved" within forty characters of
a date written as 2025-03-02, 2 March 2025 or March 2025. It reports each
line once, under CANON-2, graded warn.

A date in a task heading, a property drawer or a timestamp is not reported.
A date in a sentence that does not name a decision is not reported.
=== calibration
Not measured.
