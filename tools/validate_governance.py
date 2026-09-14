#!/usr/bin/env python3
"""Validate the ESE DIGITALS governance/continuity repository.

This tool validates structure and YAML syntax. It never changes phase, gate,
certification, or authorization state.
"""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required.")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]

required = [
    "AGENTS.md",
    "CODEX_MASTER_EXECUTION_PROMPT.md",
    "README.md",
    "governance/phase-state.yaml",
    "governance/gate-register.yaml",
    "governance/authority-matrix.yaml",
    "governance/phase-4/GATE_CROSSWALK.yaml",
    "governance/execution/CODEX_CONTINUITY_KERNEL.yaml",
    "governance/execution/CURRENT_EXECUTION_STATE.yaml",
    "governance/execution/CURRENT_OBJECTIVE.md",
    "governance/execution/NEXT_ACTIONS.md",
    "governance/evidence/INDEX.yaml",
    "governance/certification/CERTIFICATION_STATUS.yaml",
]

errors = []
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"missing: {rel}")

for p in ROOT.rglob("*.yaml"):
    try:
        yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid-yaml: {p.relative_to(ROOT)}: {exc}")

state = yaml.safe_load((ROOT / "governance/phase-state.yaml").read_text(encoding="utf-8"))
gate = yaml.safe_load((ROOT / "governance/gate-register.yaml").read_text(encoding="utf-8"))
cert = yaml.safe_load((ROOT / "governance/certification/CERTIFICATION_STATUS.yaml").read_text(encoding="utf-8"))

if state["project"]["current_gate"] != "G9.5":
    errors.append("current_gate drift: expected G9.5")
if gate["phase_4"]["current_gate"]["status"] != "IN_PROGRESS":
    errors.append("gate drift: expected G9.5 IN_PROGRESS")
if cert["certification"]["status"] != "NOT_CERTIFIED":
    errors.append("certification drift: expected NOT_CERTIFIED")
if cert["certification"]["downstream_authorization"] != "BLOCKED":
    errors.append("authorization drift: expected BLOCKED")

if errors:
    print("GOVERNANCE VALIDATION: FAIL")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("GOVERNANCE VALIDATION: PASS")
print("Current phase: PHASE_4")
print("Current gate: G9.5 / IN_PROGRESS")
print("Certification: NOT_CERTIFIED")
print("Downstream authorization: BLOCKED")
print("No governance state was modified.")
