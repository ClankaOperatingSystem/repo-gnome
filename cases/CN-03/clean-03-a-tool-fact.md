title: A method that states what a tool does
expect:
why: A fact about a tool's behaviour that affects use.
path: methods/shared-emacs.org
---
#+TITLE: Shared Emacs method

* Check equivalence and effects

Isolate every batch Emacs run, trials included. =-Q= skips init files but
still writes to the user's Emacs directory: the project list, the
auto-save list and the package manager's key store. Point each at a
disposable directory and afterwards confirm that nothing in the user's
Emacs directory is newer than the run.
