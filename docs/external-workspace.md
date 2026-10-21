# External workspace boundary

[source] Read-only inspection on 2026-10-21.

| Path | Observed role |
|---|---|
| `C:\dev\text-diffusion` | Parent workspace, not itself a git repository |
| `C:\dev\text-diffusion\ncm` | NCM checkout with staged, unstaged and untracked experimental edits |
| `C:\dev\text-diffusion\ncm-official` | Separate clean public NCM checkout at the time of inspection |
| `C:\dev\text-diffusion\ldlm-flowmap` | Team project; treat as private research context |
| `C:\dev\text-diffusion\comparison` | Existing evaluation/audit scripts and historical outputs |

Both NCM checkouts had base commit `c70274273f489abc73832b2b98584a8483b6b203`.
That SHA does not capture the modified checkout's uncommitted experiment.
Useful pointers are `ncm/experiments/README.md` and `ncm/experiments/PILOT10K.md`.

These files establish that external work exists, not that it was reverified here.
The current repository's **model implementation is not started**. Only research
tooling, source analysis and documentation are being changed. No private code,
weights, datasets or numerical experiment results are copied into this repository.
