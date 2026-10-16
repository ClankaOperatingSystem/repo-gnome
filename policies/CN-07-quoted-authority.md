policy_id: CN-07
subject: canon
summary: A rule is stated plainly, not framed as somebody's words
model_class: none
evidence: document/file
quotable_name: document
graded: yes
quotes_code: no
ceiling: warn
implemented: check
clause: CANON-8 quoted authority
---
Answered by the check `check-quoted-authority` in `scripts/`, which reports a
line of prose that frames a quotation as its author's authority, under
CANON-8, graded warn: "in NAME's words", "in NAME's formulation", "NAME's
words", "as NAME said", "as NAME put it", "NAME said:", "NAME wrote:", and
"NAME ruled", "NAME decided", "NAME deferred", "NAME asked" where a
quotation mark follows on the same line.

A line inside a task is not reported. A line in a code block or a quote
block is not reported.
=== calibration
Not measured.
