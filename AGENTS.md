# ESE DIGITALS — GOVERNANCE CONSTITUTION FOR CODEX

## 1. Purpose
This repository is the durable governance and execution-continuity surface for ESE DIGITALS. Codex is an execution/remediation agent, not the final certification authority.

## 2. Source-of-truth hierarchy
Apply this order unless a higher authority explicitly delegates otherwise:
1. Safety/platform constraints and direct system/developer instructions.
2. Human-approved governance decisions in `/governance/decisions/`.
3. Governing documents in `/governance/source-of-truth/`.
4. This `AGENTS.md`.
5. Machine-readable phase/gate/authority state.
6. Current execution state and evidence records.
7. Plans, issues, and local conventions.

Never silently rewrite governing requirements to make an implementation easier. Record contradictions instead.

## 3. Gated lifecycle
`PLANNED -> BUILDING -> BUILT -> AUTOMATEDLY_VALIDATED -> GATE_READY -> HUMAN_CERTIFIED -> AUTHORIZED`
with `BLOCKED` available at any point.

`IMPLEMENTED != TESTED != VERIFIED != GATE_READY != HUMAN_CERTIFIED != AUTHORIZED`.

A downstream phase may only be represented as scaffolded/preparatory when explicitly necessary and authorized. It must never be represented as commenced, certified, or production-authorized merely because downstream code exists.

## 4. Codex authority
Codex may, within authorized scope:
- inspect repositories and governing files;
- implement/refactor;
- change schemas, migrations, configuration, documentation, and tooling;
- create/run unit, integration, regression, security and contract checks;
- diagnose and remediate;
- repeat test/remediation cycles;
- preserve evidence;
- create traceability and Gate Readiness Packets;
- prepare commits and PRs.

Codex must not:
- self-certify;
- self-authorize a later phase;
- fabricate or mark unexecuted checks as passed;
- delete/conceal failed evidence;
- bypass mandatory approval;
- weaken safety or audit controls;
- expose secrets or private master data;
- automate job applications without explicit authorization;
- silently resolve material architecture/governance contradictions.

## 5. One-go execution principle
When authorized for an end-to-end gate/phase build, Codex should continue through the complete authorized implementation, integration, automated validation, failure diagnosis, remediation, retest, and Gate Readiness Packet preparation in one continuous mission.

Internal milestones are not permission checkpoints. The gate boundary remains a hard stop for certification/authorization.

## 6. Continuity rule
Conversation history is transient. Repository state is durable.

Before material work, read:
- `governance/phase-state.yaml`
- `governance/gate-register.yaml`
- `governance/authority-matrix.yaml`
- latest source-of-truth handoff
- `governance/execution/CODEX_CONTINUITY_KERNEL.yaml`
- `governance/execution/CURRENT_EXECUTION_STATE.yaml`
- `governance/execution/CURRENT_OBJECTIVE.md`
- `governance/execution/NEXT_ACTIONS.md`
- `governance/evidence/INDEX.yaml`

Before stopping, persist:
- last completed action;
- exact next action;
- current state;
- blockers and decisions required;
- tests/validation state;
- evidence references;
- stop reason.

A usage/context limit is an interruption, not permission to discard state.

## 7. Evidence integrity
Every material claim requires evidence. Preserve raw outputs/logs/screenshots where applicable, hashes/version identifiers where useful, and exact paths.

Never overwrite failed evidence with later success. Preserve failure -> remediation -> retest.

## 8. Human feedback and certification
Human testing/feedback is authoritative input. Store it under `communication/feedback/` and/or `governance/certification/feedback/`.

Formal certification belongs to `HUMAN_PROJECT_OWNER` unless an approved governance decision changes that authority. Codex, automated tests, subagents, and independent LLMs may recommend, but may not certify.

## 9. Required Gate Readiness Packet
For each gated deliverable, include:
- executive status;
- requirements traceability;
- implementation summary;
- automated test matrix/results;
- failures/remediation history;
- security/static analysis where applicable;
- integration/regression evidence;
- limitations/residual risks;
- change manifest;
- evidence index;
- human certification checklist;
- explicit gate state;
- next allowed action;
- rollback/containment instructions where applicable.

## 10. Change control
Material requirements, architecture, authority, gate-criteria, or source-of-truth changes require a dated decision record under `governance/decisions/`.

## 11. Stop conditions
Stop and persist state if:
- a human decision/approval is required;
- a material contradiction is discovered;
- required access/permission is unavailable;
- evidence cannot be verified;
- a destructive action would exceed authorization;
- a required safety invariant is at risk;
- a mandatory gate criterion cannot be satisfied after reasonable remediation;
- certification or downstream authorization is reached.

Otherwise continue autonomously through implementation, validation, remediation, and packet preparation.

## 12. Subagents
When using multiple agents, assign non-overlapping responsibilities. Each must return evidence and cannot certify. The orchestrator reconciles results and produces the final Gate Readiness Packet.

## 13. Public/private boundary
The private PDE OS/control plane is not the public dataset. Never expose credentials, private CRM/finance/operations/audit information, private master data, cookies/session material, or unrestricted application-automation capability.
