# Research context: concise source digest

[generated] Distilled on 2026-10-21 from chat A, chat B and Notion N1 in the
[source register](source-register.json). These sources establish research intent,
not empirical proof. N1 is marked unverified by Notion.

1. **Primary question:** NCM's conditional within-level factorization may miss useful
   dependencies; investigate a joint conditional generator while freezing the tokenizer.
   Source: N1, chat B. Paper grounding: NCM p.6, Eq.5.
2. **First experiment:** denoise the current level iteratively, preserving the outer
   coarse-to-fine order. Masked diffusion and optional remasking are candidate tools,
   not a settled claim of superiority. Source: chat B.
3. **Evaluation first:** compare quality and diversity under one pinned protocol;
   do not infer improvement from GenPPL or NFE alone. Source: N1, chat B.
4. **Representation branch:** early continuous slots should be informative and easy
   to generate; prefix reconstruction and later joint training are proposals.
   Informative prefixes do not automatically guarantee a tractable prior. Source: N1, chat A.
5. **Generation-path branch:** jointly generate a level and part of the following
   level; specify what is frozen, revisited or remasked next. Source: chat A, N1.
6. **Comparison boundary:** distinguish NCM residual code levels, HDLM vocabulary
   ancestors, and H-CDLM jointly diffused token/cluster modalities. Source: all three PDFs.

The note's reconstruction figure must be dataset-qualified: NCM Table 1 reports
99.99% for OWT and 99.86% for LM1B. This is a paper result, not our reproduction.
No model code or experiment is claimed here. RL, new encoders and full joint
training remain exploratory branches rather than requirements for the first study.
