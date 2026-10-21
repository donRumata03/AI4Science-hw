# Research context

[generated] Primary question: can iterative conditional generation improve the joint
distribution of codes inside one NCM level while keeping its tokenizer fixed?
Model implementation in this repository has not started.

- First study: freeze tokenizer, codebooks and decoder; keep levels sequential;
  denoise the current level conditioned on previous levels and visible current codes.
- Evaluate quality, diversity and compute under one protocol with a matched one-pass
  fine-tuning control. Neither low GenPPL nor low NFE alone establishes improvement.
- Later ideas: informative continuous prefixes with reconstruction losses; joint
  representation learning; generate one level and the beginning of the next together.
  These are proposals, not completed results or requirements of the first experiment.
- Distinguish residual code levels (NCM), vocabulary ancestors (HDLM), and jointly
  diffused token/cluster modalities (H-CDLM). Source cards and memory retain PDF pages.

[source] Research intent: chats
`6ad0e66b-2738-83eb-98ea-2112c0c2aacd` and
`6ad62397-44dc-83eb-9770-39f494b040c6`, plus
[Notion NCM](https://app.notion.com/p/3fa2d7fdcb1280c59884d800c22d9e03).
Notion ideas are unverified proposals. The external experimental workspace is separate;
its historical results are not reproduced or imported into this submission.
