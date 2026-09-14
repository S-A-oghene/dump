# ESE DIGITALS — Governance & Codex Continuity Dump

This repository is the **durable governance/continuity layer** for ESE DIGITALS.

It is intentionally not the application repositories.

## Start here

1. `AGENTS.md`
2. `governance/phase-state.yaml`
3. `governance/gate-register.yaml`
4. `governance/authority-matrix.yaml`
5. `governance/source-of-truth/`
6. `governance/execution/CODEX_CONTINUITY_KERNEL.yaml`
7. `governance/execution/CURRENT_EXECUTION_STATE.yaml`
8. `governance/execution/CURRENT_OBJECTIVE.md`
9. `governance/execution/NEXT_ACTIONS.md`
10. `governance/evidence/INDEX.yaml`

## Current state

PHASE_4 / BUILDING
G9.5 / IN_PROGRESS
CERTIFICATION = NOT CERTIFIED
DOWNSTREAM AUTHORIZATION = BLOCKED

## Purpose

The repository is designed to survive:
- Codex usage exhaustion;
- context exhaustion;
- chat/file limits;
- session interruption;
- agent replacement;
- human testing cycles.

A new Codex session should be able to resume from repository state without reconstructing the project from conversation history.

## Important

This dump does not replace:
- PDE OS source repository;
- Platform source repository;
- human certification;
- approved architecture decisions.

It records and governs them.

## G9.5 warning

There is an unresolved backend architecture/evidence reconciliation issue. Do not close G9.5 merely because a repository contains implementation or technical test evidence.
