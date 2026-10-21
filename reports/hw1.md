---
type: Report
---
# Homework 1: environment and context

Research: conditional diffusion inside an NCM code level with a fixed
tokenizer. The repository contains research preparation; model implementation and
training have not started. Text is maintained in English.

## Acceptance evidence

| Week | Required result | Evidence / outcome |
|---|---|---|
| 1 | Git environment; generation-verification cycle | Generated artifacts, external checks, diary and commits. Full week-1 slides are unavailable; only the summary criterion is assessed. |
| 2 | Goal, acceptance/verifier, mode/budget/context, marked constraints | AGENTS.md and research tasks specify these fields; no forced ReAct or fictional technical restrictions. |
| 3 | L1/L2/L3; >=3 checked claims; instructions and navigation | Main-paper L1, 8 L2 claims, one-sentence L3, 6 PDF-page checks, AGENTS sections and INDEX.md. |
| 4 | >=3 classes, >=2 rules, >=10 typed objects; consistent graph | 11 classes, 3 rules, typed research/source/query/author/task objects; ontology.yaml, Obsidian configuration and check_graph.py. |
| 5 | >=20 documents; 5 BM25/vector queries and analysis; executed SPARQL linked to graph | 27 local title/abstract documents, 5 ranked comparisons, saved vectors/settings, 5 SPARQL bindings with provenance and project links. |

## Search implementation

Week 5 follows search_lab.ipynb. The corpus uses titles/abstracts; three papers additionally have original PDFs. BM25 uses k1=1.2, b=0.75.
Neural retrieval uses normalized all-MiniLM-L6-v2 vectors on CPU; the model revision and full top-5 scores are saved.
The search report reviews every top-3 pair, including an off-topic motion-generation result and possible
alternate MAUVE records. No gold-set relevance metric is claimed.

Wikidata SELECT returned five machine-learning instance-class bindings. Query,
endpoint, date and raw response are retained and linked to the research methods.
Three seed metadata records were checked against PDF page 1 (title, ID, first author).

## Verification
Run: `python checks/check_structure.py`, `check_evidence.py`, `check_graph.py`, and
`check_week5.py` (the latter three also reside in checks/). Actual outputs: checks.txt.
The checks establish file integrity, evidence locations and local consistency;
semantic claim review is recorded separately in memory/verification.md.


## Links
- type: [[ontology/Report]]
- completes: [[tasks/read-ncm]]
- completes: [[tasks/develop-graph]]

## References to assignments and acceptance criterions
Week 2 slides pp.41-43; week 3 pp.70-71,74; week 4 pp.83-84; week 5 pp.86-88.
