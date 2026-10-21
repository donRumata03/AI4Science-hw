"""Check repository links and pinned PDF integrity; does not grade homework.

Run from any directory: python <repo>/checks/check_structure.py
Uses only Python's standard library. Graph type/rule validation is separate.
"""

from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md", "STATUS.md", "diary.md", "INDEX.md", "README.md",
    "docs/course.md", "docs/project.md", "docs/workflow.md",
    "docs/external-workspace.md", "library/catalog.json", "library/README.md",
    "memory/L1.md", "memory/L2.md", "memory/L3.md", "memory/verification.md",
    "ontology.yaml", ".obsidian/app.json", ".obsidian/graph.json",
    "reports/hw1.md", "reports/my_search_report.md", "tasks/research.md",
)


def main():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"Missing file: {name}")

    markdown = [p for p in ROOT.rglob("*.md")
                if not {".git", ".venv", "work"}.intersection(p.relative_to(ROOT).parts)]
    links_checked = 0
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        # Code examples contain illustrative links, so ignore fenced code blocks.
        prose = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
        prose = re.sub(r"`[^`\n]*`", "", prose)
        for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)", prose):
            target = unquote(target.strip().strip("<>"))
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            links_checked += 1
            if not (path.parent / target).exists():
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")
        for target in re.findall(r"\[\[([^\]\n]+)\]\]", prose):
            target = target.split("|", 1)[0].split("#", 1)[0]
            links_checked += 1
            candidate = ROOT / target
            if not candidate.exists() and not candidate.with_suffix(".md").exists():
                errors.append(f"Broken wiki link: {path.relative_to(ROOT)} -> {target}")

    catalog_path = ROOT / "library/catalog.json"
    if catalog_path.is_file():
        try:
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            ids = set()
            for item in catalog["documents"]:
                key = (item["arxiv_id"], item["version"])
                if key in ids:
                    errors.append(f"Duplicate document: {key}")
                ids.add(key)
                pdf = ROOT / item["pdf_path"]
                if not pdf.is_file():
                    errors.append(f"Missing PDF: {item['pdf_path']}")
                else:
                    data = pdf.read_bytes()
                    if not data.startswith(b"%PDF-"):
                        errors.append(f"Invalid PDF header: {item['pdf_path']}")
                    if sha256(data).hexdigest() != item["sha256"]:
                        errors.append(f"PDF digest mismatch: {item['pdf_path']}")
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f"Invalid catalog: {exc}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: required files, {links_checked} local links, pinned PDF digests.")
    print("Scope: structure only; article claims, graph rules and homework remain ungraded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
