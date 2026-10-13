title: A contract with a table of cases
expect:
why: The same rule as a table, one row per case.
path: methods/contract.org
---
#+TITLE: The scope contract

* Dependency direction

Which link to write:

| From  | To                            | Link                                |
|-------+-------------------------------+-------------------------------------|
| canon | own or descendant canon       | path                                |
| canon | own archive                   | =ipfs://<cid>/path=                 |
| canon | a child's archive             | the child's canon, which leads there |
| canon | anything outside the scope    | path to a rumour in its own archive |
| canon | a checkout beside the repository | none; a rumour                   |
