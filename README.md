# fde-demo-banking

> **The deliverable is in this repo**: [`project-0.1.27-agent/`](project-0.1.27-agent/) — the emitted, implemented, deployable output on the current framework (pipeline service, deploy assets, runbooks, evals, `ARCHITECTURE.md`, `RISKS.md`, `SCORECARD.md`). Start at [`project-0.1.27-agent/README.md`](project-0.1.27-agent/README.md). The no-agent baseline the framework shipped is beside it as [`project-0.1.27/`](project-0.1.27/); the earlier 0.1.26 run is kept as [`project-baseline-0.1.26/`](project-baseline-0.1.26/) and [`project/`](project/).

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
never saw. Two independent audit passes (the eighth and ninth of the
framework's series) read this run; what they found is in the framework's
[changelog](https://github.com/atulkapoor/fde-framework/blob/main/CHANGELOG.md)
and, where it changed the numbers, below.

## The engagement, as recorded

| Stage | What happened |
|---|---|
| Statement | "Route each inbound customer support message to one of seventy-seven handling queues by intent." |
| Brief | [`brief.md`](brief.md): free text in, a decision out, inside the bank's cloud account, customer data may not leave, a platform team operates it, nobody waits in real time, one outward system (the ticketing API), every route must be explainable, an unknown queue is fine if rare |
| Facts | `fde frame` read the brief; the interview answers were **authored by the person running this demo** in the roles of a platform lead and a head of support, from the brief and the dataset (customer VPC, business hours, role-based access, 500 messages a day at peak, 9,999 labelled messages -- the vendor's training split -- personal data present, p95 five seconds, explainability required). There is no real client behind them |
| Exam | `fde samples` took the 9,999 training queries as verified pairs: 6,946 golden, 17 edge cases (length extremes, rare intents, typical probe bases), 11 adversarial probes, and a 3,036-case holdout the engagement keeps and the delivery never ships. The vendor's own 3,079-query test split is kept as a second, external exam nobody at the engagement chose |
| Gates | Baseline recorded (operational figures stated by the support lead, every one marked *stated, not measured* on the SLO page); data access attested; security review recorded; `client_readiness` waived with the eval owner named |
| Architecture | `customer-vpc`; reasoning `labelled-decision` (a decision read off text with a labelled history), planning `fixed-sequence`, integration `direct-call` (not wired: the ticketing call answers 501 by name) behind `role-scoped-authority` governance and a `decision-log`, evaluation `labelled-metrics`, `terraform-module` provisioning, `structured-logs` |

## What was delivered, measured

`fde scorecard project-0.1.27-agent --holdout engagements/banking/artifacts/holdout.jsonl --external engagement-prep/vendor-test.jsonl`,
at the two abstain margins ([`SCORECARD.md`](project-0.1.27-agent/SCORECARD.md),
[`SCORECARD-margin-1.0.md`](project-0.1.27-agent/SCORECARD-margin-1.0.md)):

| | Shipped baseline, no agent (`project-0.1.27`) | After the implement loop (`project-0.1.27-agent`) | Same, at a 1.0-nat abstain margin |
|---|---|---|---|
| Scorecard | 22 of 24 rows hold | 23 of 24 | 22 of 24 |
| Golden, in-sample | 84.1% (abstained 10%) | 91.6% (abstained 4.3%) | -- |
| **Holdout, 3,036 cases never shipped** | 73.7%, abstaining 16.1%, **87.9% on the answered** | 77.5%, abstaining 10.5%, **86.6% on the answered** | 73.8%, abstaining 18.2%, **90.2% on the answered** |
| **Vendor test split, 3,079 cases (external exam)** | 72.2% | **75.8%** | 71.6% |
| Beats the bank's recorded 88% first-pass accuracy on the answered | no, by 0.1 point | no, by 1.4 points | **yes** |
| Generalisation gap (golden in-sample minus holdout) | 10.4 points | 14.2 points | -- |
| Adversarial probes, 11 | 10 of 11, one abstained under mutation | 11 of 11, none followed | -- |
| A valid request through the edge answers, and says why | yes | yes | yes |

Reading it honestly:

- **This is an assist-mode router, not an autonomous one.** At the
  default margin the deliverable routes 89% of messages and is right on
  86.6% of those, short of the bank's own first-pass bar. At a one-nat
  margin it hands 18% of messages to a person and is right on 90.2% of the
  rest, which clears the bar. The card says which, and neither number
  is quoted without its abstain share.
- **The out-of-sample numbers are the numbers.** The golden score is
  in-sample (the baseline is fitted on that file) and the card marks it
  so; the holdout and the vendor split are what the system can do on
  messages it never saw. The gap between them is on the card.
- **What the agent changed.** One file: word bigrams over the same
  fitted baseline and a smaller smoothing constant, chosen by
  cross-validation on golden (its own docstring). Under the loop's fence
  it could not touch the exam, the tests, the contract or the boundary,
  and its round was refused once for a lint error the tests caught.
- **The literature gap.** A TF-IDF and logistic-regression baseline
  reaches about 85% on this dataset; fine-tuned encoders reach the low
  nineties. This deliverable is a bag-of-words baseline plus one agent
  round, and the framework's fine-tuning path is the next step, measured
  on the same holdout and vendor split.

## The operating loop, closed

0.1.28 carries the record past the build, and this repository is the first
place the whole loop has run in public. Everything below is in
[`field/loop.txt`](field/loop.txt) exactly as the commands printed it; the
record it wrote is [`engagements/banking/lifecycle.jsonl`](engagements/banking/lifecycle.jsonl),
[`engagements/banking/incidents.jsonl`](engagements/banking/incidents.jsonl) and
[`project-0.1.27-agent/VALUE.md`](project-0.1.27-agent/VALUE.md).

**The field.** The delivered build (`project-0.1.27-agent`) was booted as
its unit would boot it, on the author's laptop, and two streams were sent
through it over HTTP. Its journal -- the `answered` lines the service
writes for every request -- is what the record reads, and both journals are
committed ([`field/`](field/); they carry the decision, the margin and the
cue tokens, never the message).

| Stream | Requests | Abstained | Right on the answered | Drift |
|---|---|---|---|---|
| 1: the vendor's test split, 3,079 messages across all 77 queues ([summary](field/stream-1-summary.json)) | 3,079, all 200 | 11.5% | 85.7% (75.8% overall, the card's external-exam figure to the decimal) | none: mix distance 0.08 from the golden, abstention 11.5% against 10.5% on the holdout |
| 2: a card-reissue campaign -- 200 messages from five card queues only ([summary](field/stream-2-summary.json)) | 200, all 200 | 12.0% | 81.8% | **decision mix**: distance 0.81 from the golden; `inc-001` opened |

**The trail.** `fde stage` computed each stage off the record and appended
every transition:

| Transition | Why |
|---|---|
| start -> pilot | gates pass, 9,999 pairs seeded, a 3,036-case holdout drawn, data access attested, a build with its exam, a scorecard whose out-of-sample rows hold, the edge answering a valid request |
| pilot -> production | `fde deployed` attested where it runs: *the author's laptop, over HTTP on 127.0.0.1, for the field drill; the bank's VPC is not on this record* |
| production -> pilot | `fde drift` on stream 2 opened `inc-001` (decision mix); an open incident pulls production back |
| pilot -> production | the holdout was scored again as the incident asked (77.5% on 3,036 cases, unchanged, regression from the last card: none), and `inc-001` was closed by name with what was done: the shift was in the field's mix, not in the router; no rebuild |

`fde outcomes` reads the same trail back: 4 transitions, 2 implement rounds
logged, 0 reversals, 1 incident opened and closed, no outcome recorded.

**The value.** `fde value` wrote the business case from the recorded
baseline and the holdout row, at an assumed 30 an hour, 160 hours to
build, 300 a month to run and a person re-checking 20% of automated
routes: 1,074 hours and 32,220 a year saved, payback in 2.0 months, the
answered accuracy 85.3% to 87.8% at 95%. The document names what it rests
on before the total. Four lines are *stated*, not measured, because the
bank's own figures were (annual volume, cycle time, labour, the first-pass
error rate); four are *assumed* by the caller. And one line is the honest
one: at the default margin the router's 13.4% error on what it routes is
above the bank's stated 12%, so *net errors* is positive -- about 1,500
wrong routes a year that a person would not have made. The 1.0-nat margin
clears the bar at 18% abstention; the value at that margin is the same
command against that card.

**What this is and is not.** The deployment is a laptop and the record says
so in the attestation itself. Both streams are the vendor's public test
split, not the bank's traffic, and the campaign is a drill: five queues
chosen to move the mix the way a real campaign week would. The whole loop
ran in one day, so days-to-pilot reads 0. No adoption figure exists because
no client exists, and the stage stops at production for that reason rather
than pretending past it.

## What this run found in the framework

Six defects the framework's own suite could not have shown, each fixed
and pinned in 0.1.26 before the first numbers were quoted, and six more
from the ninth audit pass, fixed in 0.1.27:

- Seventy-seven intents were read as structured records, so the first
  build had no reasoning component and an exam at 0.0%.
- The brief's own words -- "routed to a handling queue", "by intent" --
  were not recognised as a decision.
- An intent name written into a message steered the router, because
  underscore-joined labels were not stripped; stripping every mention
  then cost two points on customers stating the intent in their own
  words, so a label is now stripped only where it is dictated.
- A governance module no other build had emitted failed lint.
- The implement loop scored the holdout against the in-sample golden bar
  and refused a better implementation; it never ran the deliverable's own
  tests; its fence did not cover the tests or the contract.
- The router routed a greeting, gibberish and a French message to the
  commonest queue at a 0.02-nat margin; it now abstains below a margin,
  and every routed answer carries the top labels, the margin and the
  tokens that carried it.
- The scorecard scored a component that memorised the exam files at
  17 of 17; it now carries a generalisation-gap row, an external exam,
  and the engagement's own error-rate bar.

## The implement loop

Both runs are logged beside the projects
([`implement-log-run1-0.1.26.md`](implement-log-run1-0.1.26.md),
[`implement-log-run2-0.1.26.md`](implement-log-run2-0.1.26.md),
[`project-0.1.27-agent/ops/implement-log.md`](project-0.1.27-agent/ops/implement-log.md)).
The coding agent was Claude Code reading its brief on stdin. On 0.1.26
the first run cleared its bar and was refused as "memorised" because the
holdout inherited the in-sample bar (a framework defect, fixed); the
second run went red on a lint error the deliverable's own tests caught,
then green. On 0.1.27, under the corrected gate, the loop took the
holdout from 73.7% to 77.5% in two rounds.

## Reproduce it

```bash
python3 prepare.py                                   # fetches Banking77 into engagement-prep/
python3 -m venv venv && venv/bin/pip install "fde-framework>=0.1.28"
venv/bin/fde start banking --statement "Route each inbound customer support message to one of seventy-seven handling queues by intent."
venv/bin/fde frame banking --file brief.md
venv/bin/fde samples banking --file engagement-prep/pairs.jsonl
venv/bin/fde baseline banking --file baseline.yaml   # then data-access, security-review, waive, ask (see engagements/banking/)
venv/bin/fde build banking --out project
venv/bin/fde scorecard project --holdout engagements/banking/artifacts/holdout.jsonl --external engagement-prep/vendor-test.jsonl

# the operating loop: boot the service, send traffic, keep its journal (stderr), then
venv/bin/fde stage banking --project project
venv/bin/fde deployed banking --note "where it runs and who put it there"
venv/bin/fde drift banking --journal field/stream-2-card-campaign.log --project project
venv/bin/fde incident banking close inc-001 --note "what was done"
venv/bin/fde value banking --project project --hourly-cost 30 --review-share 0.2
venv/bin/fde outcomes banking --project project
```

The eval files embed the dataset's text and are not committed; they
regenerate from `prepare.py` and a build, and every digest is in each
project's `evals/manifest.json`.
