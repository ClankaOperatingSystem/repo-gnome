title: A rule with one exception
expect:
why: One exception is not a layer.
path: methods/contract.org
---
#+TITLE: The scope contract

Archive records cite other archived items by =ipfs://<cid>/path=, never
by path, except within a collection, where links stay relative paths
that the collection's CID fixes.
