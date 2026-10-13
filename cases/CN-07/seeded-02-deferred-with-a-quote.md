title: An item that quotes the deferral
expect: CANON-8
grade: warn
why: "The maintainer deferred it: ..." frames a quotation, outside a task.
path: index.org
---
#+TITLE: The root

* Propagating a container's changes to its children

A child spawned without its inheritance from its container shows the
need. The maintainer deferred it: "we can worry about this later". The
scope boundary rule forbids a child from knowing its parent, so the
container must propagate changes.
