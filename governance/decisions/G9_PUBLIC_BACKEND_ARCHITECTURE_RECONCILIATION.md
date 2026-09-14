# G9 Public Backend Architecture Reconciliation — OPEN

Status: OPEN / HUMAN DECISION REQUIRED

## Contradiction

Evidence sets currently describe two public-backend patterns:

A. Worker -> authenticated Apps Script read-only bridge -> private `JOBS` data -> public-safe projection.

B. Worker-native public Opportunity API -> D1 -> public-safe projection, with Apps Script outside the request path.

## Current governing disposition

No approved decision record selects one route as the final canonical architecture.

The V4 handoff remains the current controlling operational state for G9.5.

## Required decision

The human authority must decide:
- canonical public request path;
- authoritative data source;
- synchronization/provenance policy;
- migration/sequence if both routes are retained;
- required evidence reruns;
- gate-state treatment of existing technical evidence.

## Prohibited shortcut

Do not infer the final architecture from whichever repository contains newer-looking code.
