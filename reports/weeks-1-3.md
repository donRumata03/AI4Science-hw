# Weeks 1-3: acceptance evidence

[generated] Research deliverables completed on 2026-10-21 under source-grounded
criteria. Week 1-specific slides are unavailable; only its confirmed summary scope
can be assessed. The complete week 1 rubric remains unknown. Course acceptance by
an instructor and scientific correctness are not inferred from automated passes.

| Week | Criterion source | Current result |
|---|---|---|
| 1 | W3 p.74 / W5 p.88: git environment and generation-verification cycle | Confirmed summary criterion met: existing git snapshot -> generated research contracts/context -> external verifier -> diary and commit |
| 2 | W2 pp.41-43; W3 p.74: goal, criteria/verifier, budget/mode/context, restrictions, journal/git | Contract artifact met: AGENTS and research task contracts specify these fields; structure/language checks passed |
| 3 | W3 pp.70-71: L1/L2/L3, at least 3 source checks, >=5 instruction sections, unknown context, index/git | Artifact criteria met: section-level L1, 8 L2 claims, one-sentence L3, 6 reviewed claims, 10 AGENTS sections, unknown-context section, index and git |

The model implementation has not started. Verification scripts are research tooling.
The course notebook's live API/model-frequency exercises are not reported as executed.

## Foundation execution record

Request: reframe the repository around the research itself, distill both chats and N1,
and maintain all project files in English. Actual artifacts: AGENTS.md, project/context
notes, source register, task protocols and per-task acceptance/verifier/mode sections.
External check: `python checks/check_structure.py`, exit 0, 82 local links and pinned
PDF hashes. An English prose scan also passed. Commit evidence is in git history.
The unavailable week 1 presentation prevents a claim against its complete rubric.

## Week 2: concrete research task contract

Outcome: summarize the primary NCM paper for the within-level dependence hypothesis.
Acceptance: main-section L1, 5-10 L2 claims, one-sentence L3 and at least three source
checks, with tokenizer state and evaluation scope preserved. Verifier: check_evidence.py
plus source-page reading. Mode: extraction pipeline followed by claim audit. Budget:
one named summary deliverable per block. Context: AGENTS, STATUS, INDEX, the pinned
PDF and current research scope. Boundaries: no source edits, invented findings or training.
Execution record: the artifacts below were produced, externally checked and recorded
in the diary. The foundation snapshot is d4870b5; the source-review snapshot follows
as a separate commit visible in git history. No forced ReAct transcript is required.

## Week 3: criterion-by-criterion evidence

| Acceptance criterion | Actual artifact | Result |
|---|---|---|
| L1 by paper sections | memory/L1.md, main Sections 1-5 with explicit review boundary | Met |
| L2 with 5-10 claims | memory/L2.md, C1-C8 | Met: 8 |
| L3 in one line/sentence | memory/L3.md | Met |
| At least three source-verified statements | memory/verification.md and verification.json | Met: 6; PDF text and rendered pages reviewed |
| At least five AGENTS sections | AGENTS.md | Met: 10 |
| What the agent cannot infer | Dedicated AGENTS section and external-workspace note | Met |
| Navigation and git | INDEX.md, linked source notes and source-review commit | Met |

Corrections retained: Eq.5 is a model factorization, not a data-independence theorem;
Table 1 reconstruction is 99.86% for LM1B and 99.99% for OWT; per-sample entropy is
not corpus n-gram diversity. These are source-reading outcomes, not new experiments.

## Reproducible commands and limits

```powershell
python -m pip install -r checks/requirements.txt
python checks/check_structure.py
python checks/check_evidence.py
python checks/agent_loop_demo.py
git log --oneline -3
```

The commands were run with system Python 3.12 / pypdf 5.9.0. The first checks validate
files, PDF integrity, source-anchor locations and document shape. Meaning/scope was
reviewed against source pages separately. A negative control sent claim C7 to p.9
instead of Table 1 on p.8 and was rejected. The isolated test did not modify the PDFs.
Actual command outputs and the environment record are in [validation.json](validation.json).

[agent-loop.md](agent-loop.md) documents four executed offline driver scenarios and
the deterministic-fixture limitation. Live model-frequency/API exercises from the
original course notebook were not run and are not claimed as completed.

## Additional requested research work

Three original PDFs are present with unchanged hashes. The two named chats and
Notion page N1 were read, and only a concise research digest was retained. Bounded
method reviews and [hierarchy-comparison.md](hierarchy-comparison.md) cover the three
papers without declaring a full appendix/proof audit or a cross-paper benchmark ranking.
All maintained project prose and graph class names are English. The implementation
status is explicitly not started; existing external experiments remain separate.
