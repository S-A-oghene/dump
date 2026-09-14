# Evidence Structure

Store evidence by phase/gate/run.

Recommended structure:
`governance/evidence/PHASE_4/G9.5/<execution-id>/`

Each run should contain:
- `RUN_METADATA.yaml`
- raw test outputs/logs;
- screenshots where relevant;
- verification summaries;
- remediation history;
- immutable references/hashes.

Do not overwrite failed evidence.
