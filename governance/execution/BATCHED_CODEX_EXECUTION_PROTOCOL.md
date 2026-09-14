# ESE DIGITALS — Batched Codex Execution Protocol

## Mission model

A large authorized task is executed as one Codex mission with internal batches. Codex does not stop for every internal milestone.

### Batch 0 — Bootstrap
Load governance, source-of-truth documents, continuity state, and authority.
Verify repository HEAD/status and current gate.

### Batch 1 — Reconcile
Compare current source/evidence across relevant repositories and governance.
Classify findings:
- RESOLVED_BY_DECISION
- EVIDENCE_GAP
- OPEN_CONTRADICTION
- VERIFIED_FACT

Do not resolve contradictions by inference.

### Batch 2 — Implement
Perform all authorized implementation/remediation needed for the current objective.
Group changes logically and avoid repeated inspection of unchanged material.

### Batch 3 — Validate
Run all applicable automated tests:
- unit
- integration
- regression
- contract/schema
- security/static checks
- build/deployment checks
- deterministic smoke tests

On failure, diagnose -> remediate -> retest. Preserve failure history.

### Batch 4 — Verify integrations
Where authorized, validate routes, services, data boundaries, API contracts, and end-to-end automated behavior.
Do not convert automated evidence into human certification.

### Batch 5 — Prepare Gate Readiness Packet
Produce/update the packet with:
- status
- traceability
- implementation summary
- tests/results
- failure/remediation history
- security/static analysis
- integration/regression evidence
- residual risks
- change manifest
- evidence index
- human certification checklist
- explicit gate state
- next allowed action

### Batch 6 — Stop/handoff
Stop if human authority, material unresolved contradiction, required permission, unverifiable evidence, or certification/authorization is reached.
Persist exact continuation state before ending.

## Efficiency rules

- Prefer broad inspection and batched tool calls.
- Parallelize independent tests where safe.
- Read unchanged governance files once per batch.
- Reuse evidence using immutable references/hashes.
- Do not re-upload repository files to chat for continuity.
- Do not spend execution budget proving unchanged facts.
- Preserve raw evidence and summarize it in packets.

## Session interruption protocol

If Codex reaches a usage/context boundary:
1. persist CURRENT_EXECUTION_STATE;
2. persist NEXT_ACTIONS;
3. update evidence index;
4. record stop reason;
5. leave the workspace in a reproducible state.

The next session resumes from the repository, not the prior conversation.
