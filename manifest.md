agent_id: repository
summary: What a repository's maintained documents say, and whether they state the present
subjects: document/file, scope/canon
policies: CN-01, CN-02, CN-03, CN-04, CN-05, CN-06, CN-07, CN-08, CN-09, CN-10
---

This file describes the gnome to whatever reads it. The lines above
the three dashes are read by a bugflow server and by the format tests;
the text below is for a person.

- `agent_id` is the reviewer's id on a server. The commit status on a
  pull request has this name.
- `summary` is one line saying what the policies read.
- `subjects` lists the kinds of evidence the policies ask for. A consumer
  renders the subjects it can and reports a policy it cannot.
- `policies` lists every policy. A policy judges a repository on a server
  only when the server's declarations also list it for that repository;
  the repo-gnome-tidy skill applies them all.
