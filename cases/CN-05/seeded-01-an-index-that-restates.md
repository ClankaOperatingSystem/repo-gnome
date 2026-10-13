title: A doctrine index whose entries restate their rules
expect: CANON-6
grade: warn
why: Each entry carries the rule in a paragraph beside the link to its home, and a degree of force.
path: methods/doctrine.org
---
#+TITLE: Doctrine

The repository's rules, gathered in one maintained index. Each entry names
a rule, points to its authoritative home and says how it is checked.

* Rules

** Canon links stay within their scope
:PROPERTIES:
:CUSTOM_ID: D-canon-links
:SOURCE: [[file:contract.org::#dependency-rule][Scope contract: dependency rule]]
:FORCE: forbidden
:CHECK: audit links
:END:
Canon links only to its own scope's canon, its children's canon and its
own archive. The rule covers paths in code and data as well as document
links.

** Canon states the present
:PROPERTIES:
:CUSTOM_ID: D-present-tense
:SOURCE: [[file:contract.org::#present-tense][Scope contract: canon states the present]]
:FORCE: required
:CHECK: judgment
:END:
No provenance, supersession notes, adoption status, defensive hedges or
links that recount rather than serve the work.
