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
at the two abstain margins ([`SCORECARD-margin-0.5.md`](project-0.1.27-agent/SCORECARD-margin-0.5.md)
at the default margin, [`SCORECARD.md`](project-0.1.27-agent/SCORECARD.md) at the
1.0-nat margin the deployment now ships, since the stop drill below):

| | Shipped baseline, no agent (`project-0.1.27`) | After the implement loop (`project-0.1.27-agent`) | Same, at a 1.0-nat abstain margin |
|---|---|---|---|
| Scorecard | 22 of 24 rows hold | 23 of 24 | 23 of 25 (re-scored on 0.1.35: [`field/rescore-0.1.35.txt`](field/rescore-0.1.35.txt)) |
| Golden, in-sample | 84.1% (abstained 10%) | 91.6% (abstained 4.3%) | -- |
| **Holdout, 3,036 cases never shipped** | 73.7%, abstaining 16.1%, **87.9% on the answered** | 77.5%, abstaining 10.5%, **86.6% on the answered** | 73.8%, abstaining 18.2%, **90.2% on the answered** |
| **Vendor test split, 3,079 cases (external exam)** | 72.2% | **75.8%** | 71.6% |
| Beats the bank's recorded 88% first-pass accuracy on the answered | no, by 0.1 point | no, by 1.4 points | on accuracy yes (90.2%); **on coverage no**: 81.8% answered against the 97% the bank's own exception rate sets |
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
| 3: the vendor's split again, at the shipped 1.0-nat margin ([summary](field/stream-3-summary.json)) | 3,079, all 200 | 20.1% | 89.7% (the card's external row to the decimal) | none; four forecasts held, see below |

**The trail.** `fde stage` computed each stage off the record and appended
every transition:

| Transition | Why |
|---|---|
| start -> pilot | gates pass, 9,999 pairs seeded, a 3,036-case holdout drawn, data access attested, a build with its exam, a scorecard whose out-of-sample rows hold, the edge answering a valid request |
| pilot -> production | `fde deployed` attested where it runs: *the author's laptop, over HTTP on 127.0.0.1, for the field drill; the bank's VPC is not on this record* |
| production -> pilot | `fde drift` on stream 2 opened `inc-001` (decision mix); an open incident pulls production back |
| pilot -> production | the holdout was scored again as the incident asked (77.5% on 3,036 cases, unchanged, regression from the last card: none), and `inc-001` was closed by name with what was done: the shift was in the field's mix, not in the router; no rebuild |
| production -> stopped | `fde stop-when`: the author's condition `answered_accuracy < 0.88` (the bank's stated first-pass accuracy) fired against the default-margin card, 86.6% on the answered ([`field/stop-1.txt`](field/stop-1.txt)) |
| stopped -> production | the deployment's `ABSTAIN_MARGIN` set to 1.0 and the build scored again at that margin ([`field/rescore-margin-1.0.txt`](field/rescore-margin-1.0.txt)): 90.2% on the answered, abstaining 18.2%; both conditions clear ([`field/stop-2.txt`](field/stop-2.txt)) |

`fde outcomes` reads the same trail back: 6 transitions, 2 implement rounds
logged, 0 reversals, 1 incident opened and closed, no outcome recorded.

**The value.** `fde value` wrote the business case from the recorded
baseline and the shipped card, at an assumed 30 an hour, 160 hours to
build, 300 a month to run and a person re-checking 20% of automated
routes: 982 hours and 29,448 a year saved, payback in 2.2 months, the
answered accuracy 89.0% to 91.3% at 95%. The document names what it rests
on before the total. Four lines are *stated*, not measured, because the
bank's own figures were (annual volume, cycle time, labour, the first-pass
error rate); four are *assumed* by the caller. *Net errors* is now
negative -- about 2,160 fewer wrong routes a year than the people made --
because the shipped margin routes only what it is 90.2% right on. At the
default margin the same line was positive (13.4% error against the bank's
stated 12%), which is what the stop condition below caught.

**The stop.** 0.1.32 made stop a legitimate outcome, and the record here
has been stopped once. Two conditions went on it, the author's, read off
the brief: `answered_accuracy < 0.88`, the bank's stated first-pass
accuracy, and `abstain_rate > 0.25`, because a message routed to unknown
"is fine as long as it is rare". Against the card at the default 0.5-nat
margin the first fired -- 86.6% on the answered -- and `fde stage`
recorded production -> stopped ([`field/stop-1.txt`](field/stop-1.txt)).
The answer was a configuration, not a rebuild: the deployment now ships
`ABSTAIN_MARGIN=1.0` (`deploy/env.example`), the build was scored again
at that margin ([`field/rescore-margin-1.0.txt`](field/rescore-margin-1.0.txt)),
and both conditions clear ([`field/stop-2.txt`](field/stop-2.txt)), so the
stage returned to production. The card's own regression row says **no**
-- holdout 77.5% -> 73.8% -- because more messages now go to a person;
that is the trade the condition asked for, and the card says it rather
than hiding it. The first run of this drill also found a framework
defect: recording stop conditions created a partial contract file, the
eighth gate's reason changed, the waiver granted against the old reason
lapsed, and the stage dropped to discovery. 0.1.33 fixed it, with a test,
and the one stray transition was removed from the trail.

**The people.** `fde stakeholders` ([`field/stakeholders.txt`](field/stakeholders.txt))
reads the engagement's people off the record: two of the five roles were
heard, both voiced by the author (the README's "Facts" row says so, and the
stakeholder entries repeat it); the eval owner, the user and the skeptic
were never asked; and every attestation, the waiver and the incident closure
carry nobody's name, because the drill ran before `--by` existed. A real
engagement would have a name on each. `fde history`
([`field/history.txt`](field/history.txt)) is the same record as one page,
in order.

**The debt.** 0.1.30 added an eighth gate, the outcome contract: who owns
the number the system exists to move, its value today, its target, how it
is measured, by when. On this record it is waived, with the reason where a
reader will find it: the brief names the number (median time to first
substantive reply, 26 hours, stated) but nobody at the bank set a target,
and there is no bank. `fde debt` ([`field/debt.txt`](field/debt.txt)) then
lists what the engagement rests on that nobody has settled: 13 items --
two standing waivers, five entries with nobody's name on them, three roles
never heard, and three environment facts the platform lead said and nobody
measured (no accelerator, no cluster, no container competence). None
blocks the build or production; the waivers age from today.

**The coverage rule.** 0.1.35 closed a loophole an outside reading found:
the card's baseline row held on accuracy on what the system answered, with
no coverage requirement, so a router that abstained on nine cases in ten
and got the tenth right would have "beaten" the bank. The row now judges
both axes, and the coverage floor comes from the bank's own record: its
people hand 3% of messages to the unknown queue, so the system may hand on
no more than that. Re-scored at the shipped margin the row reads: 90.2% on
the answered against 88.0%, coverage 81.8% against a floor of 97.0%,
n=3,036, correct 2,240, wrong 244, abstained 552, overall 73.8%, 95%
interval 88.9% to 91.3% on the answered -- and does not hold. So the
honest sentence about this deliverable is now: it routes what it routes
better than the bank's people do, and it routes less of it. Both stop
conditions still clear, because the author set the abstention condition at
25%, not at the bank's 3%; a client would set that number, and the card
would then say the same thing the stop condition does.

**The forecast.** 0.1.36 lets an engagement say what it expects before it
measures, and be held to it. Four forecasts went on this record before
stream 3 ran ([`field/forecast-1.txt`](field/forecast-1.txt)): the field
abstain rate between 16% and 22%, the field error rate under 1%, the
decision mix within 0.15 of the golden. Stream 3 was then driven through
the service at the shipped margin and the forecasts scored
([`field/forecast-2.txt`](field/forecast-2.txt)): all four held, mean
signed error -0.011. Every one of them is marked *made after a card
existed*, and that mark is the point: the card's external row had already
shown 20.1% abstention at this margin, so these were informed guesses
about whether the service in the field matches the card, not forecasts
about an unknown. The first uninformed forecast belongs to the first
engagement that records one before its build is scored.

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
python3 -m venv venv && venv/bin/pip install "fde-framework>=0.1.36"
venv/bin/fde start banking --statement "Route each inbound customer support message to one of seventy-seven handling queues by intent."
venv/bin/fde frame banking --file brief.md
venv/bin/fde samples banking --file engagement-prep/pairs.jsonl
venv/bin/fde baseline banking --file baseline.yaml   # then data-access, security-review, waive, ask (see engagements/banking/)
venv/bin/fde build banking --out project
venv/bin/fde scorecard project --holdout engagements/banking/artifacts/holdout.jsonl --external engagement-prep/vendor-test.jsonl --coverage-floor 0.97   # the bank's own exception rate is 3%

# the operating loop: boot the service, send traffic, keep its journal (stderr), then
venv/bin/fde stage banking --project project
venv/bin/fde deployed banking --note "where it runs and who put it there"
venv/bin/fde drift banking --journal field/stream-2-card-campaign.log --project project
venv/bin/fde incident banking close inc-001 --note "what was done"
venv/bin/fde value banking --project project --hourly-cost 30 --review-share 0.2
venv/bin/fde outcomes banking --project project
venv/bin/fde stakeholders banking && venv/bin/fde history banking
venv/bin/fde debt banking                # what nobody has settled, with an owner and an age
venv/bin/fde stop-when banking --when "answered_accuracy < 0.88" --project project   # exit 1 and a STOP stage when it fires
venv/bin/fde predict banking --when "field_abstain_rate <= 0.22" --project project    # before the stream; then --journal <log> to score it
```

The eval files embed the dataset's text and are not committed; they
regenerate from `prepare.py` and a build, and every digest is in each
project's `evals/manifest.json`.
