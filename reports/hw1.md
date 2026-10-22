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

## Examples of queries to local context

Five queries run against the local library; the table shows each method's first result.

| Query | BM25 top result | Vector top result |
|---|---|---|
| How does NCM construct hierarchical residual codes and condition each level? | NCM | NCM |
| How can masked diffusion generate discrete codes jointly with a frozen tokenizer? | NCM | Re-evaluating Confidence Remasking in Masked Diffusion Language Models |
| Which remasking samplers can revise already generated diffusion tokens? | CoDR: Training-Free Confidence-Drift Remasking | Re-evaluating Confidence Remasking in Masked Diffusion Language Models |
| How do semantic vocabulary clusters differ from learned latent hierarchies? | Aligned and realistic latent diffusion for text-to-motion generation | HDLM (2510.08632) |
| How should MAUVE and diversity evaluate generated text beyond perplexity? | MAUVE: Measuring the Gap Between Neural Text and Human Text | On the Usefulness of Embeddings, Clusters and Strings for Text Generator Evaluation |

Both methods retrieve NCM for the architecture query. For remasking, their top-three
results share NAVIRA and Remask, Don't Replace. For hierarchy comparison, vector
search retrieves HDLM and H-CDLM, while BM25 ranks an off-topic motion paper first.
The evaluation query retrieves MAUVE through both methods. Full rankings and scores:
[search report](my_search_report.md).

[source] Wikidata query executed on 2026-10-21 at `https://query.wikidata.org/sparql`:

```sparql
SELECT ?item ?itemLabel ?class ?classLabel WHERE {
 VALUES ?item { wd:Q2539 }
 ?item wdt:P31 ?class .
 SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
```

Five bindings were returned. The query note links to the local machine-learning
concept, which is connected to NCM through `researchField`; endpoint, date and raw
response are retained in `library/retrieval/`.

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
