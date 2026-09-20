# Service objectives

Two buckets, because reporting one is half a story. A technical number nobody outside the team cares about, and a business number nobody inside it can move directly -- and a system healthy on the first while the second does not move is a system nobody will renew.

## Technical

- **Latency** — p95 under 5000ms at expected peak. Measured at the edge, not inside a component, because that is where somebody experiences it.
- **Availability** — business hours: planned windows outside them are free.
- **Evaluation score** — the golden layer at or above the threshold CI gates on. A drop here is a regression whether or not anything is down.
- **Adversarial score** — tracked separately and never averaged in. Scoring well on golden and badly on adversarial means nobody has attacked it yet.

## Business

- **The thing that should move** — stated by whoever asked for this, in their words, before it was built. If nobody can say what should change, that is the finding.

## Baseline

**Captured.** The numbers to beat, by their recorded definitions:

- **volume** — 10000 messages/month (inbound support messages needing a queue (stated by the support lead; the dataset itself is 13,083 messages)) — **stated, not measured**
- **cycle_time_per_unit_seconds** — 45 s (message read to queue assigned, by a triage agent (stated, from the team's own estimate)) — **stated, not measured**
- **labour_hours_per_week** — 30 h/week (triage agents reading and routing (stated)) — **stated, not measured**
- **rework_rate** — 0.12 share (messages re-routed after a wrong first queue (stated, from re-route counts)) — **stated, not measured**
- **exception_rate** — 0.03 share (messages sent to the unknown queue (stated)) — **stated, not measured**
- **error_rate** — 0.12 share (the re-route rate is the first-pass error rate (stated)) — **stated, not measured**
- **business_metric** — 26 hours (median time to first substantive reply (stated)) — **stated, not measured**

7 of these figures are stated rather than measured. The acceptance protocol's bar is the measured error rate; capture it by the same definition before quoting a delta.
- sampled: n=200, one week of re-route logs, read by the support lead (stated, not re-measured here)

Re-measure by identical definitions in 60 days. A comparison that quietly changes a definition is a comparison with its thumb on the scale.
