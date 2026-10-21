# NCM source verification

[generated] Six L2 claims were checked against original PDF text and rendered pages
on 2026-10-21. This is assistant source review, not independent human acceptance or
experimental reproduction. Machine-readable locations are in
[verification.json](verification.json); the pinned PDF hash is in the library catalog.

| L2 claim | PDF location | Source-review outcome | Scope retained or corrected |
|---|---|---|---|
| C2 | p.6, Section 3.2, Eq.5 | Verified | Conditional independence is the generator factorization; it is not a theorem about real code dependencies |
| C3 | p.6, Section 3.3, Eqs.7-8 | Verified | Residual downsampling, nearest-code lookup and cumulative reconstruction are distinct operations |
| C4 | p.7, Nested dropout, Eq.9 | Verified | A sampled prefix receives reconstruction/VQ losses; ease of prior generation remains an open research property |
| C5 | p.7, Section 3.4, Algorithms 1-2 | Verified | All-level one-pass training must not be confused with sequential coarse-to-fine inference |
| C7 | p.8, Table 1 | Verified with dataset qualification | LM1B is 99.86%, OWT is 99.99%; a generic 99.99% reconstruction statement is overbroad |
| C8 | p.9, Section 4.2 and Figure 5 | Verified within scope | Reference scorer is GPT-2-large; reported entropy is mean per-sample unigram entropy, not corpus n-gram diversity or MAUVE |

## Verifier boundary

`python checks/check_evidence.py` checks the pinned PDF hash, page bounds, L2 IDs,
and the presence of short source anchors on those pages. It also checks the English
policy and summary shape. Anchor matches establish location, not scientific entailment;
the table above records the separate source-reading judgment.

## Remaining uncertainty

No conclusion is drawn about whether the proposed denoiser improves quality, how much
compute it requires, or whether continuous-prefix alternatives are better. Those are
future experiments. The numerical reconstruction values above are published evidence.
