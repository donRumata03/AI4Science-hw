# AI4Science research submission

Research: conditional diffusion inside an NCM level. Model code has not started;
this package contains the required environment, memory, graph and retrieval evidence.

- [Final report](reports/hw1.md)
- [Search report](reports/my_search_report.md)
- [File index](INDEX.md)
- [Research context](docs/project.md)

Run from the repository root:
```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r checks/search-requirements.txt
.venv/Scripts/python.exe checks/check_structure.py
.venv/Scripts/python.exe checks/check_evidence.py
.venv/Scripts/python.exe checks/check_graph.py
.venv/Scripts/python.exe checks/check_week5.py
```

`search_lab_ncm.ipynb` inspects the executed own-topic notebook adaptation.
`checks/run_search_lab.py` refreshes retrieval; saved results allow offline verification.
All maintained project files are English. Source PDFs remain original.
