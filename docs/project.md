# Research scope

[generated] Can conditional diffusion improve the quality/diversity/compute frontier
of Next-Concept Modeling by modeling dependencies inside one discrete code level?

## Primary study

Keep the NCM tokenizer, codebooks, reconstruction operators and text decoder fixed.
Keep levels sequential. Replace one-pass current-level prediction with iterative
denoising conditioned on earlier levels and the visible/noisy current-level codes.
The input is `(previous-level reconstruction, noisy current-level codes, noise state)`;
the output is a sampled complete level. This is a hypothesis, not an implemented result.

Before implementation, establish the relevant paper assumptions, an evaluation
protocol, a matched one-pass fine-tuning control, and explicit compute accounting.
MAUVE, n-gram diversity, GenPPL, entropy, NFE and wall time serve different purposes;
their definitions and preprocessing must be pinned before comparisons.

## Deferred branches

- Group adjacent levels, or jointly generate a level and the beginning of the next;
  define remasking and conditioning without ground-truth leakage.
- Build informative continuous latent prefixes using reconstruction losses, then
  consider joint representation/generator training.
- Change conditioning compression, generation paths, or alignment only as separate ablations.

## Current deliverables

Paper reviews, a verified summary hierarchy, literature-search records, and a concise
research design. Model implementation has not started in this repository.
See [context](research-context.md) for attribution and [task protocols](task-protocols.md)
for acceptance and verification. Course packaging is tracked separately.
