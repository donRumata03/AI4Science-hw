---
type: Source
arxiv_id: "2510.08632"
version: v1
source_url: https://arxiv.org/abs/2510.08632v1
accessed: 2026-10-21
---
# Next Semantic Scale Prediction via Hierarchical Diffusion Language Models

[source] Cai Zhou, Chenyu Wang, Dinghuai Zhang, Shangyuan Tong, Yifei Wang, Stephen Bates, Tommi Jaakkola. [Official record](https://arxiv.org/abs/2510.08632v1).

## Review scope

[generated] PDF pp.1-6 for hierarchy, transition construction, reverse process and training; proof/benchmark reproduction excluded.

## Representation

A surjective mapping assigns word tokens to coarser semantic ancestors. The diffusion state can be a word, cluster or mask, and positions may occupy different scales.

## Generation and conditioning

Forward transitions coarsen token identities; reverse denoising refines them. See p.2 overview, p.4 Eq.4 and pp.5-6 Sections 3.2-3.3.

## Relevance

Provides a distinct semantic diffusion-state design. Applying it to NCM code IDs would require defining and validating an ancestor map.

## Limits

A vocabulary hierarchy is not a learned sequence-level residual tokenizer; no matched quality ranking or full theorem verification is claimed.

## Links
- type: [[ontology/Source]]
- describes: [[notes/hdlm]]
- storedIn: [[library/pdf/2510.08632v1.pdf]]
- writtenBy: [[notes/author-2510.08632]]
