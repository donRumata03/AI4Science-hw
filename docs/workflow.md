# Research workflow

1. Read AGENTS.md, STATUS.md and INDEX.md.
2. Select one research task and retain its fixed acceptance criteria.
3. Load only its source pages and relevant notes.
4. Produce a bounded artifact; label source facts, user intent and generated proposals.
5. Run its verifier and review scientific scope manually against the cited pages.
6. Rewrite STATUS.md, append diary.md and commit the reason for the change.

## Example: paper review

```text
Review HDLM against the within-level NCM hypothesis. Identify the represented random
variables, forward/reverse process and conditioning. Cite PDF pages. State which
parts transfer to fixed NCM codes and which would require a different representation.
Acceptance and verifier: tasks/compare-hierarchies.md. Write all artifacts in English.
```

## Example: summarization

```text
Summarize the main NCM paper by section into memory/L1.md, reduce it to 5-10 claims
in L2.md and one sentence in L3.md. Verify at least three claims from PDF pages;
separate model factorization from assumptions about real data. Record corrections.
Acceptance and verifier: tasks/read-ncm.md. Update status and append the diary.
```

## Example: literature search (not executed yet)

```text
Find up to five primary papers relevant to remasking discrete latent codes. Retain
the query, source identifiers, access status and relevance decisions. Do not turn
abstracts or suggested references into claims of a completed full-text review.
Acceptance and verifier: tasks/search-library.md.
```
