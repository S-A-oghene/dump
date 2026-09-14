# ESE DIGITALS — Governance Baseline / Replacement Dump

Baseline date: 14 September 2026.
Purpose: durable governance and Codex continuity replacement for the `dump` repository.

## 1. Controlling state

- PHASE_4 / BUILDING
- G9.5 / IN_PROGRESS
- BUILD_AUTHORIZATION = YES (Phase 4 only)
- CERTIFICATION_STATUS = NOT CERTIFIED
- DOWNSTREAM_AUTHORIZATION = BLOCKED

The latest controlling V4 handoff remains authoritative for current operational status.

## 2. Governing sources included

This replacement contains:
- `AGENTS.md` — constitutional Codex execution rules.
- `governance/source-of-truth/Ese_Digitals_V4_Migration_Master_Session_Context_2026-09-13.md`.
- `governance/source-of-truth/Ese_Digitals_Phase_4_Opportunity_Intelligence_Engine_Master_Build_Manual_v2_2.docx`.
- machine-readable phase/gate/authority state.

## 3. Known material contradictions

### Public backend topology
One evidence line describes a Worker-to-Apps-Script authenticated read-only bridge, while platform-local implementation/evidence describes a Worker-native D1 public path.

No approved decision record currently selects the final canonical topology.

### Gate evidence chronology
Later-looking platform technical evidence exists, but the V4 handoff remains the controlling current state and records G9.5 IN_PROGRESS.

No formal human reconciliation/certification record currently resolves this.

## 4. Governance gaps

- formal architecture reconciliation decision;
- formal G9 certification/attestation record;
- complete per-gate/subgate crosswalk with evidence;
- Phase 4 requirements traceability and exit packet;
- human acceptance feedback records where testing has occurred;
- production authorization decision.

## 5. Continuity solution

This repository separates:
- constitution (`AGENTS.md`);
- machine state (`phase-state.yaml`, `gate-register.yaml`, `authority-matrix.yaml`);
- source-of-truth documents;
- execution state;
- evidence index;
- traceability;
- decision records;
- certification records;
- communication/feedback;
- change control.

The conversation is not the source of durable project state.

## 6. Non-goals

This repository does not change application source, deployment topology, gate status, certification authority, or phase authorization.
