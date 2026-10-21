# Hierarchical text generation research

[generated] Research question: can iterative conditional generation improve the joint
distribution of codes inside an NCM level while preserving its learned tokenizer?
This repository currently contains literature analysis and research design.
**Model implementation: not started.** Research tooling lives in `checks/`; `src/` is empty.

## Start here

- [Research scope](docs/project.md): the primary question and deferred branches.
- [Concise context](docs/research-context.md): distilled ideas from the two chats and Notion.
- [Current status](STATUS.md) and [file map](INDEX.md).
- [Task protocols](docs/task-protocols.md): acceptance, verifier, mode and stop conditions.

## Research outputs

Three pinned PDFs are in `library/pdf/`; provenance and SHA-256 are in
[catalog.json](library/catalog.json). NCM is the primary paper for the L1/L2/L3
memory hierarchy. HDLM and H-CDLM are comparison sources, not interchangeable
implementations of the proposed NCM experiment.

```powershell
Set-Location C:\dev\Education\AI4Science
python -m pip install -r checks/requirements.txt
python checks/check_structure.py
```

Existing external experiments are documented only by pointers in
[external-workspace.md](docs/external-workspace.md). No training is launched here.

Course evidence is a secondary view of the same research outputs:
[course requirements](docs/course.md) and [weeks 1-3 report](reports/weeks-1-3.md).
Weeks 4-5 remain future work. No remote repository is configured.
