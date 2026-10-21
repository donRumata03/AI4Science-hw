---
type: Report
---
# Three hierarchy constructions: bounded method review

[generated] Reviewed method pages of three pinned PDFs on 2026-10-21. This comparison
supports research design, not a benchmark ranking or exhaustive reproduction.

| Dimension | NCM: 2610.14162v1 | HDLM: 2510.08632v1 | H-CDLM: 2610.08738v1 |
|---|---|---|---|
| Hierarchy | Learned residual code sequences with increasing lengths | Token identities map to coarser vocabulary ancestors | Tokens and deterministic clusters form two same-length modalities |
| Generative state | Current discrete level, conditioned on cumulative earlier reconstruction | Discrete token/cluster/mask states; positions may occupy different semantic scales | Concatenated continuous representations of token/cluster modalities |
| Order | Sequential across levels; one factorized parallel sample within a level | Progressive reverse diffusion through semantic scales; no single global NCM-level schedule | Both modalities denoised jointly; schedules/sampler may differ by modality |
| Primary locations | p.6 Eqs.3-8; p.7 Algorithms 1-2 | p.2 overview; p.4 Eq.4; pp.5-6 reverse process and CT-ELBO | p.5 Figure 2 and Section 4.1; p.6 Sections 4.2-4.3 |
| Transfer limit | Natural fixed-tokenizer test bed for iterative current-level generation | A semantic ancestor map over NCM code IDs would need to be established, not assumed | Same-length auxiliary channels do not reproduce NCM's short coarse levels or frozen-prefix schedule |

## Implications for our study

1. The clean first question changes within-level generation while retaining NCM's
   representation. It does not require inventing a new hierarchy at the same time.
2. HDLM demonstrates a different place to introduce hierarchy: diffusion states in
   a semantic vocabulary. H-CDLM uses auxiliary hierarchical representations as
   coupled denoising signals. Neither establishes the benefit of our exact adaptation.
3. Jointly generating a level and the next prefix is a separate proposal. Its known
   conditions must exclude clean target information; remasking policy must be explicit.
4. A future comparison needs identical text preprocessing and controls for additional
   optimization and compute. Published numbers across papers are not ranked here.

## Review limits

Core method/representation claims were read from the original PDFs. Proofs, all
appendices, full benchmark reproduction and software ports are outside this review.
NCM's six audited summary claims are documented separately in memory/verification.md.

## Links
- type: [[ontology/Report]]
- completes: [[tasks/compare-hierarchies]]
