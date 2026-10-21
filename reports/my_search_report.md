---
type: Report
---
# Personal-library retrieval

[generated] Executed on 2026-10-21 using the section-14 workflow of search_lab.ipynb: 27 local title/abstract documents, five own queries, BM25 and neural cosine retrieval. Three seed papers additionally have original PDFs. This is not a full-text search over 27 PDFs.

## Method

Adapted cells: 5 (OpenAlex/abstract recovery), 9 (tokenization), 13 (BM25), 19 (normalized neural vectors), 34 (SPARQL), 45 (own topic). Original notebook SHA-256: `3f5ad49cc6f260cadc2a6687a430933894ed82066e4968eec06aa5fe0fea0b8f`. Encoder: `sentence-transformers/all-MiniLM-L6-v2`, revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, CPU, 384 dimensions, max input 256 tokens. BM25: k1=1.2, b=0.75. Raw requests, corpus, vectors and ranked scores are in `library/retrieval/`.

## Q1: How does NCM construct hierarchical residual codes and condition each level?

| Rank | BM25 | Vector |
|---|---|---|
| 1 | Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation (2610.14162; 13.473) | Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation (2610.14162; 0.322) |
| 2 | Next Semantic Scale Prediction via Hierarchical Diffusion Language Models (2510.08632; 8.545) | Corrective Diffusion Language Models (W7116092176; 0.263) |
| 3 | Remask, Don't Replace: Token-to-Mask Refinement in Diffusion Language Models (W7155194316; 4.784) | Denoising Hierarchical Representations: Joint Continuous Diffusion for Language Modeling (2610.08738; 0.262) |

[generated] Review: Both methods rank NCM first. Lexical retrieval also promotes HDLM through shared hierarchy vocabulary; vector retrieval adds related corrective/joint-denoising work. NCM is directly relevant; neighboring methods need a full-text check. Top-3 overlap: 1/3 (agreement, not a relevance score).

## Q2: How can masked diffusion generate discrete codes jointly with a frozen tokenizer?

| Rank | BM25 | Vector |
|---|---|---|
| 1 | Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation (2610.14162; 5.856) | Re-evaluating Confidence Remasking in Masked Diffusion Language Models (W7164370247; 0.529) |
| 2 | Simple and Effective Masked Diffusion Language Models (W4415800813; 5.600) | NAVIRA: Decoupled Stochastic Remasking for Masked Diffusion Language Models (W7163641485; 0.481) |
| 3 | Diffusion Language Model for Recommendation (W7170357931; 5.138) | STaRR: Spatial-Temporal Token-Dynamics-Aware Responsive Remasking for Diffusion Language Models (W7119901757; 0.478) |

[generated] Review: BM25 surfaces NCM and MDLM, which are useful architectural anchors. Vector retrieval favors remasking variants, relevant to iterative decoding but incomplete answers to the frozen-tokenizer condition. Neither method alone establishes transfer compatibility. Top-3 overlap: 0/3 (agreement, not a relevance score).

## Q3: Which remasking samplers can revise already generated diffusion tokens?

| Rank | BM25 | Vector |
|---|---|---|
| 1 | CoDR: Training-Free Confidence-Drift Remasking for Diffusion Language Models (W7220962774; 8.271) | Re-evaluating Confidence Remasking in Masked Diffusion Language Models (W7164370247; 0.588) |
| 2 | NAVIRA: Decoupled Stochastic Remasking for Masked Diffusion Language Models (W7163641485; 5.008) | NAVIRA: Decoupled Stochastic Remasking for Masked Diffusion Language Models (W7163641485; 0.584) |
| 3 | Remask, Don't Replace: Token-to-Mask Refinement in Diffusion Language Models (W7155194316; 4.988) | Remask, Don't Replace: Token-to-Mask Refinement in Diffusion Language Models (W7155194316; 0.567) |

[generated] Review: Both retrieve remasking work and share useful candidates, but their first choices differ. This is a strong literature-discovery query; claims of correctness or superiority require reading the actual sampler definitions. Top-3 overlap: 2/3 (agreement, not a relevance score).

## Q4: How do semantic vocabulary clusters differ from learned latent hierarchies?

| Rank | BM25 | Vector |
|---|---|---|
| 1 | Aligned and realistic latent diffusion for text-to-motion generation (W7169721105; 6.604) | Next Semantic Scale Prediction via Hierarchical Diffusion Language Models (2510.08632; 0.457) |
| 2 | Next Semantic Scale Prediction via Hierarchical Diffusion Language Models (2510.08632; 5.775) | Denoising Hierarchical Representations: Joint Continuous Diffusion for Language Modeling (2610.08738; 0.416) |
| 3 | LDSeq: Latent Diffusion Models for Sequence to Sequence Text Generation (W4392824136; 4.471) | On the Usefulness of Embeddings, Clusters and Strings for Text Generator Evaluation (W4281642786; 0.409) |

[generated] Review: Vector retrieval surfaces both HDLM and H-CDLM. BM25 promotes a text-to-motion paper: a genuine false positive caused by overlapping latent/alignment vocabulary. The distinction between text conditioning and text generation must be screened manually. Top-3 overlap: 1/3 (agreement, not a relevance score).

## Q5: How should MAUVE and diversity evaluate generated text beyond perplexity?

| Rank | BM25 | Vector |
|---|---|---|
| 1 | MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers (W3212136196; 7.118) | On the Usefulness of Embeddings, Clusters and Strings for Text Generator Evaluation (W4281642786; 0.576) |
| 2 | An Information Divergence Measure Between Neural Text and Human Text (W3170816811; 6.686) | MAUVE: Human-Machine Divergence Curves for Evaluating Open-Ended Text Generation. (W3127186743; 0.549) |
| 3 | An Empirical Comparison of Generation Quality and Diversity Between Discrete Diffusion and Autoregressive Text Generation (W7160826062; 6.456) | MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers (W3212136196; 0.528) |

[generated] Review: Both return MAUVE/evaluation records. Vector retrieval also finds the embeddings/clusters evaluation paper. Multiple MAUVE records may be alternate versions: deduplicate at the work level before making a final bibliography or estimating coverage. Top-3 overlap: 1/3 (agreement, not a relevance score).

## External graph and verification

SPARQL SELECT on Wikidata Q2539 returned 5 instance-of bindings. The query, raw JSON, endpoint and date are stored and linked by a GraphQuery note to the machine-learning Concept, which is connected to the NCM methods. This is modest taxonomy enrichment, not validation of the scientific hypothesis.

Three seed-source metadata records (NCM, HDLM, H-CDLM) were checked against primary PDF page 1: title, arXiv ID and first author; the existing PDF hashes remain unchanged. OpenAlex candidates retain access/review scope and are not falsely marked full-text reviewed.

## Limits

No relevance gold set was constructed; no Precision@k/nDCG claim is made. The corpus is small and query-selected; metadata duplicates, tokenizer truncation and nearby non-text-generation work affect coverage. This is the notebook baseline, not a production RAG system.

## Links
- type: [[ontology/Report]]
- completes: [[tasks/search-library]]
