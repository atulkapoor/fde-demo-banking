"""Regenerate the engagement's data artifacts from the public Banking77 dataset.

Banking77 (PolyAI, CC BY 4.0) is 13,083 real customer queries to a retail
bank's support channel, each labelled with one of 77 intents -- the routing
decision a support desk makes before anyone answers. The framework sees it
as a decision read off free text with a labelled history: every query is a
verified pair whose output is the intent.

The vendor's own split is kept: the 10,003 training queries are the pairs
handed to `fde samples` (which draws the engagement's holdout from them);
the 3,080 test queries are a second, external exam nobody at the
engagement chose, scored at the end with the same harness.

Deterministic: same files in, same pairs out. Nothing here is redistributed;
the files are fetched from the source repository.
"""
import csv
import json
import subprocess
from pathlib import Path

SOURCE = "https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/master/banking_data/"
PREP = Path(__file__).resolve().parent / "engagement-prep"
PREP.mkdir(exist_ok=True)


def fetch(name: str) -> list[dict]:
    target = PREP / name
    if not target.exists():
        subprocess.run(["curl", "-sS", "--max-time", "120", SOURCE + name, "-o", str(target)],
                       check=True)
    with target.open(newline="") as handle:
        return list(csv.DictReader(handle))


def pairs(rows: list[dict], prefix: str) -> list[dict]:
    seen: set[str] = set()
    out = []
    for n, row in enumerate(rows):
        text = row["text"].strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append({"id": f"{prefix}-{n:05d}", "input": text,
                    "output": {"intent": row["category"]}, "verified": True})
    return out


train = pairs(fetch("train.csv"), "q")
test = pairs(fetch("test.csv"), "t")
with (PREP / "pairs.jsonl").open("w") as handle:
    for pair in train:
        handle.write(json.dumps(pair) + "\n")
with (PREP / "vendor-test.jsonl").open("w") as handle:
    for pair in test:
        handle.write(json.dumps(pair) + "\n")
intents = sorted({p["output"]["intent"] for p in train})
print(f"{len(train)} training pairs, {len(test)} vendor test pairs, {len(intents)} intents")
