"""Offline driver exercise inspired by the course Agent in Code notebook.

The policy is a deterministic fixture, not a language model. This demonstrates
external acceptance, protected writes and repeat detection, not model quality.
No network, inference credentials, training or source-file mutation is used.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_case(documents, truncated=False, protected_write=False, repeats=False):
    env = {"catalog.json": json.dumps(documents), "result.txt": ""}
    expected = len(documents)  # Fixed from the complete source before any tool call.
    original = env["catalog.json"]
    trace = []
    actions = [("read", "catalog.json")]
    if repeats:
        actions = [("wait", "job"), ("wait", "job")]
    previous = None
    for action in actions:
        if action == previous:
            trace.append({"event": "repeat_stopped"})
            return {"accepted": False, "reason": "repeat_stopped", "source_unchanged": True, "trace": trace}
        previous = action
        if action[0] == "wait":
            trace.append({"event": "observation", "value": "still running"})
            continue
        observed = documents[:2] if truncated else json.loads(env["catalog.json"])
        trace.append({"event": "read", "observed_documents": len(observed)})
        target = "catalog.json" if protected_write else "result.txt"
        if target != "result.txt":
            trace.append({"event": "write_blocked", "path": target})
            return {"accepted": False, "reason": "protected_write", "source_unchanged": env["catalog.json"] == original, "trace": trace}
        env[target] = str(len(observed))
        trace.append({"event": "write", "path": target, "value": env[target]})
    accepted = env["result.txt"] == str(expected)
    trace.append({"event": "external_verifier", "expected": expected, "accepted": accepted})
    return {"accepted": accepted, "reason": "verified" if accepted else "wrong_result", "source_unchanged": env["catalog.json"] == original, "trace": trace}


def main():
    catalog = json.loads((ROOT / "library/catalog.json").read_text(encoding="utf-8"))
    docs = [x["arxiv_id"] for x in catalog["documents"]]
    cases = {
        "complete_observation": run_case(docs),
        "silent_truncation": run_case(docs, truncated=True),
        "protected_source_write": run_case(docs, protected_write=True),
        "repeated_action": run_case(docs, repeats=True),
    }
    assert cases["complete_observation"]["accepted"]
    assert not cases["silent_truncation"]["accepted"]
    assert cases["protected_source_write"]["reason"] == "protected_write"
    assert cases["repeated_action"]["reason"] == "repeat_stopped"
    assert all(x["source_unchanged"] for x in cases.values())
    print(json.dumps({"policy": "deterministic fixture; no live model", "source_count": len(docs), "cases": cases}, indent=2))


if __name__ == "__main__":
    main()
