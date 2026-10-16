title: A README that tells a new maintainer what to read first
expect:
why: Each step tells the reader what to read and what to do with it; none is about tending the document.
path: README.md
---
# Review policies

## Your first week

1. Read the doctrine, `rules/references/doctrine/`, in filename order.
   It is the standard that most findings cite.
2. Read one policy from top to bottom, `RV-01`: its header, its
   instructions to the model and its calibration notes. Then read its
   cases in `rules/cases/RV-01/`. Each case says in its `why` line what
   the judge should see in it.
3. Run the checks:

       uv run --with pytest pytest
