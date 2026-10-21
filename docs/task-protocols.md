# Research task protocols

[generated] The research objective is defined in `project.md`. Course weeks label
evidence after the work; they are not instructions to invent an artificial study.

| Task | Output and acceptance | Verifier | Mode and stop |
|---|---|---|---|
| Paper review | Three pinned PDFs; each card distinguishes representation, corruption/generation, conditioning, relevance and limitations, with PDF pages | PDF hashes/title checks; inspect cited pages; compare against source, not prior chat prose | Plan then execute; stop the bounded review after the three cards and comparison are supported |
| Summarization | NCM L1 by main-paper section, L2 with 5-10 claims, one-sentence L3; at least three independently located claim checks with pages | `check_evidence.py` checks anchors and hashes; source-page review checks meaning and scope | Extraction pipeline followed by claim audit; stop when L1/L2/L3 are consistent and corrections recorded |
| Literature search | Each included record has a stable ID, accessible text or explicit access status, version, relevance and provenance; do not claim searches that were not run | Reopen primary records, deduplicate IDs, spot-check metadata; retain query/output | Search -> screen -> record; one named question and at most five new candidates per block |
| Research design | A concise hypothesis, fixed vs changed components, controls, metrics, costs and falsification conditions | Trace each premise to a paper or explicitly label it a proposal; check for confounded comparisons | Plan and evidence review; stop before training when design assumptions remain unresolved |

Every task records: outcome, acceptance, verifier, mode, boundaries, stop and result.
The shared boundaries and language rule live in AGENTS.md. Record decisions and
evidence summaries; a private chain-of-thought transcript is not a research artifact.

Automation verifies file/anchor consistency. It does not certify semantic truth,
scientific novelty, user acceptance or an experimental improvement.
