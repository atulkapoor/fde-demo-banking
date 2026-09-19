# fde-demo-banking

> **The deliverable is in this repo**: [`project/`](project/) — the emitted, implemented, deployable output (pipeline service, deploy assets, runbooks, evals, `ARCHITECTURE.md`, `RISKS.md`, `SCORECARD.md`). Start at [`project/README.md`](project/README.md). The no-agent baseline the framework shipped before the implement loop ran is kept beside it as [`project-baseline-0.1.26/`](project-baseline-0.1.26/).

An industry use case through
[fde-framework](https://github.com/atulkapoor/fde-framework), on real
data: **support intent routing for a retail bank**. Every customer
message that reaches the bank's app chat has to be routed to one of
seventy-seven handling queues before an agent or an automation picks it
up. The data is [Banking77](https://github.com/PolyAI-LDN/task-specific-datasets)
(PolyAI, CC BY 4.0): 13,083 real customer queries, each labelled with the
intent the support team assigned. Nothing is redistributed here;
[`prepare.py`](prepare.py) fetches it.

The point of this run is the framework's own claim, measured: that what it
emits is production grade, or says exactly where it is not. Every number
below is produced by the deliverable's own harness or by
`fde scorecard`, and the out-of-sample ones are on cases the deliverable
never saw.

## The engagement, as recorded

| Stage | What happened |
|---|---|
| Statement | "Route each inbound customer support message to one of seventy-seven handling queues by intent." |
| Brief | [`brief.md`](brief.md): free text in, a decision out, inside the bank's cloud account, customer data may not leave, a platform team operates it, nobody waits in real time, one outward system (the ticketing API), every route must be explainable |
| Facts | `fde frame` read the brief; `fde ask` recorded the platform lead's and the head of support's answers (customer VPC, business hours, role-based access, 500 messages a day at peak, 9,999 labelled messages, personal data present, p95 five seconds, explainability required) |
| Exam | `fde samples` took the 9,999 training queries as verified pairs: 6,946 golden, 17 edge cases (length extremes, rare intents, typical probe bases), 11 adversarial probes, and a 3,036-case holdout the engagement keeps and the delivery never ships. The vendor's own 3,079-query test split is kept as a second, external exam nobody at the engagement chose |
| Gates | Baseline recorded (operational figures stated by the support lead, marked as stated); data access attested; security review recorded; `client_readiness` waived with the eval owner named |
| Architecture | `customer-vpc`; reasoning `labelled-decision` (a decision read off text with a labelled history), planning `fixed-sequence`, integration `direct-call` behind `role-scoped-authority` governance and a `decision-log`, evaluation `labelled-metrics`, `terraform-module` provisioning, `structured-logs` |

## What the framework shipped before any agent touched it

The emitted reasoning component is a fitted multinomial naive Bayes over
the bank's own labelled messages. Its scores, measured by the harness on
the build under `project-baseline-0.1.26/`:

| Layer | Cases | Score | Reading |
|---|---|---|---|
| Golden (in-sample: the baseline is fitted on this file) | 6,946 | 88.8% | majority rate 1.9%, macro-F1 0.876 |
| Holdout (out-of-sample, never shipped) | 3,036 | **78.5%** | majority 1.9%, macro-F1 0.781 |
| Vendor test split (external, not the recorded holdout; the harness said so) | 3,079 | **76.2%** | macro-F1 0.753 |
| Edge cases | 17 | 47.1% | equals the layer's majority rate: the extremes are where the baseline fails |
| Adversarial probes | 11 | 100% | zero injections followed, on bases the baseline gets right |

`fde scorecard project-baseline-0.1.26 --holdout ...`: **16 of 17
measured properties hold**; the one that does not is the edge layer.
The full card is in [`project-baseline-0.1.26/SCORECARD.md`](project-baseline-0.1.26/SCORECARD.md).

## What this run found in the framework

Four defects the framework's own suite could not have shown, each fixed
and pinned in 0.1.26 before the numbers above were produced:

- **Seventy-seven intents were read as structured records.** The contract
  inferred a decision from a one-field output only up to five distinct
  values. The first build had no reasoning component at all, and its
  exam scored 0.0%. A label set is now recognised by repetition -- every
  value repeats and there are far fewer values than pairs -- however many
  labels there are.
- **The brief's own words were not recognised.** "Routed to a handling
  queue", "triage", "by intent" now read as a decision.
- **An intent name written into a message steered the router.**
  `card_arrival` is the two cue words "card" and "arrival" joined by an
  underscore; the label-phrase rule only stripped labels joined by spaces.
  One injection was followed until labels were matched the way they
  tokenise.
- **A governance module no other build had emitted failed lint.** The
  role-scoped-authority template carried two blank lines where one was
  wanted; the shape is now part of the framework's acceptance suite.

## The implement loop

`fde implement project --holdout engagements/banking/artifacts/holdout.jsonl
--check "python evals/harness.py --min-score 0.92 ..."` -- a bar above
the shipped baseline's 88.8%, so the agent had to do better than what it
was handed. The coding agent was Claude Code, reading its brief on stdin,
inside the loop's fence (the evals, boundary and decision documents are
hashed and restored if touched).

| Round | What happened |
|---|---|
| 1 | Red. The agent rewrote the reasoning component: token features plus word bigrams over the same fitted baseline, the golden score up to 95.4% (in-sample), edge cases up to 64.7%. |
| 2 | The check cleared its bar -- and the loop refused it: **holdout red**. |

That refusal was the framework's own defect, found by this run and fixed
in 0.1.26 before the run continued: the loop scored the holdout against
the golden bar, and the golden score is in-sample wherever the baseline
is fitted on it. The implementation had in fact raised the holdout from
78.5% to 81.3%. A second defect surfaced beside it: the loop's check was
the harness alone, so the round's code carried a lint error behind a
green exam. The deliverable's own tests -- now including lint -- run
first as the floor beneath the harness.

The loop was run again on the same project under the corrected gate:

| Round | What happened |
|---|---|
| 1 | Red: own tests red (the lint error). The agent fixed the one line. |
| 2 | **Green**, holdout green, "the file the build recorded". One minute. |

## What was delivered, measured

`fde scorecard project --holdout engagements/banking/artifacts/holdout.jsonl`:
**17 of 17 measured properties hold** ([`project/SCORECARD.md`](project/SCORECARD.md)).

| | Shipped baseline (no agent) | After the implement loop |
|---|---|---|
| Golden, in-sample | 88.8% | 95.4% |
| **Holdout, 3,036 cases never shipped** | 78.5% | **81.3%** (majority 1.9%, macro-F1 0.79) |
| **Vendor test split, 3,079 cases** | 76.2% | **80.2%** (macro-F1 0.800) |
| Edge cases, 17 | 47.1% | 64.7% |
| Adversarial probes, 11 | 100% | 100%, none followed |
| Lint, own tests, exam record, edge probes, environment | hold | hold |

Reading it honestly: an eighty-percent intent router over seventy-seven
queues, with every route explained by the scores it was made on, is what
a bag-of-words baseline plus one agent round buys. The published
literature on this dataset reaches the low nineties with fine-tuned
encoders; the framework's fine-tuning path is the next step, and the
holdout and the vendor split are where it would be measured. The
baseline's stated operational figures are marked as stated, not
measured, on the SLO page; the residency and hosting facts came from an
interview and are marked asserted in `RISKS.md`.
