"""Locate reviewed evidence and check research-memory shape; no semantic grading.

Dependency: pypdf from checks/requirements.txt. Source judgments are recorded in
memory/verification.md; a matching text anchor alone does not prove a claim.
"""

from hashlib import sha256
import json
from pathlib import Path
import re
import sys

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def normalized(text):
    return re.sub(r"\s+", " ", text).casefold()


def main():
    errors = []
    catalog = json.loads((ROOT / "library/catalog.json").read_text(encoding="utf-8"))
    evidence = json.loads((ROOT / "memory/verification.json").read_text(encoding="utf-8"))
    paper = next(x for x in catalog["documents"] if x["arxiv_id"] == evidence["paper_id"])
    pdf = ROOT / paper["pdf_path"]
    if sha256(pdf.read_bytes()).hexdigest() != paper["sha256"]:
        errors.append("PDF hash differs from the reviewed version")
    if paper["version"] != evidence["version"]:
        errors.append("Evidence and catalog versions differ")
    reader = PdfReader(pdf)
    l2 = (ROOT / "memory/L2.md").read_text(encoding="utf-8")
    ids = re.findall(r"^\d+\. \*\*(C\d+) -", l2, re.M)
    if not 5 <= len(ids) <= 10 or len(ids) != len(set(ids)):
        errors.append("L2 needs 5-10 unique numbered claim IDs")
    checks = evidence["checks"]
    if len(checks) < 3 or len({x["claim_id"] for x in checks}) != len(checks):
        errors.append("Need at least three distinct reviewed claims")
    for item in checks:
        cid, page = item["claim_id"], item["pdf_page"]
        if cid not in ids or item["judgment"] != "verified" or not item["scope"]:
            errors.append(f"Invalid claim record: {cid}")
        if not 1 <= page <= len(reader.pages):
            errors.append(f"Page out of bounds: {cid}")
            continue
        text = normalized(reader.pages[page - 1].extract_text() or "")
        for anchor in item["anchors"]:
            if normalized(anchor) not in text:
                errors.append(f"Source anchor absent: {cid}, page {page}, {anchor}")
    l1 = (ROOT / "memory/L1.md").read_text(encoding="utf-8")
    if len(re.findall(r"^## ", l1, re.M)) < 5:
        errors.append("L1 lacks section-level coverage")
    l3 = (ROOT / "memory/L3.md").read_text(encoding="utf-8").splitlines()
    if len([line for line in l3 if line.startswith("[generated]")]) != 1:
        errors.append("L3 needs one generated summary line")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    if "Write all project files in English" not in agents:
        errors.append("English-language policy missing")
    if len(re.findall(r"^## ", agents, re.M)) < 5 or "What the agent cannot infer" not in agents:
        errors.append("Required instruction sections missing")
    for path in ROOT.rglob("*"):
        if not path.is_file() or {".git", ".venv", "work"}.intersection(path.relative_to(ROOT).parts):
            continue
        if path.suffix in {".md", ".py", ".json", ".yaml", ".txt"}:
            if re.search(r"[\u0400-\u04ff]", path.read_text(encoding="utf-8")):
                errors.append(f"Non-English Cyrillic prose: {path.relative_to(ROOT)}")
    if list((ROOT / "src").glob("*.py")):
        errors.append("Model implementation appeared while status says not started")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: {len(ids)} L2 claims; {len(checks)} reviewed evidence locations; L1/L3; English policy.")
    print("Scope: evidence location/integrity and document shape; no semantic proof or human acceptance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
