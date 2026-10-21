---
type: Source
arxiv_id: "2610.08738"
version: v1
source_url: https://arxiv.org/abs/2610.08738v1
accessed: 2026-10-21
---
# Denoising Hierarchical Representations: Joint Continuous Diffusion for Language Modeling

[source] Mathias Ollu, Nikos Komodakis. [Official record](https://arxiv.org/abs/2610.08738v1).

## Review scope

[generated] PDF pp.4-8 for continuous setup, hierarchical method, evaluation and cluster ablations; full appendices not reviewed.

## Representation

Token and deterministic cluster sequences have the same sequence length. Their continuous encodings are concatenated by channel and denoised by one network.

## Generation and conditioning

Joint diffusion of both modalities with possible per-modality schedules and samplers. See p.5 Figure 2 and Section 4.1, p.6 Sections 4.2-4.3.

## Relevance

Shows how an auxiliary semantic view can guide denoising. It does not implement sequential short NCM levels or our fixed-tokenizer within-level adaptation.

## Limits

Core modality/schedule claims are reviewed; published benchmark gains are not independently reproduced and are not used to rank against NCM.

## Links
- type: [[ontology/Source]]
- describes: [[notes/h-cdlm]]
- storedIn: [[library/pdf/2610.08738v1.pdf]]
