title: A glossary that says the files use its words
expect:
why: The opening sentence tells the reader how the words are used in the files, which is about the subject, not about tending the document.
path: README.md
---
# Review policies

## Words

Each thing has one word here, and the files use the same one.

- Policy: one question that a model is asked about a pull request, and
  the clauses that the question judges. It is one file of `policies/`.
- Case: an example pull request, stored with the answer that a correct
  judge gives it.
- Grade: how bad a finding is, `warn` or `fail`.
