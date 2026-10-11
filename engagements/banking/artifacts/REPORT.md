# banking: decision brief

Written by `fde report` on 2026-10-12 from the record at `engagements/banking`. Every figure below is read off that record; nothing here is estimated. Where a section quotes a command, it is what the command prints today, and running it again is the way to check.

## The problem as stated

The first statement, as the client put it.

> Route each inbound customer support message to one of seventy-seven handling queues by intent.

## Where the engagement stands

The stage is computed from the evidence on the record, not declared.

```text
banking: production

  ok discovery
       ok a problem statement: Route each inbound customer support message to one of seventy-seven handling que...
  ok validation
       ok the gates pass or are waived on the record: all pass
       ok the exam is seeded from the client's pairs: 9999 pairs
       ok a holdout the delivery never ships: 3036 cases
       ok data access attested: the bank's support log export returned 9,999 labelled messages (Banking77 train 
  ok prototype
       ok a build with its exam record: project-0.1.27-agent
  ok pilot
       ok a scorecard on record: scorecard.json
       ok the out-of-sample rows hold: 73.8% on 3036 cases (majority 1.9%; abstained 18.2%, 90.2% on the answered)
       ok the edge answers a valid request: 200 "card_arrival"
  ok production
       ok a deployment on record: served on the author's laptop over HTTP on 127.0.0.1 by the author, for the fiel
       ok no open incident: none open
  -- adoption
       NO an adoption figure measured in the field: none: fde outcome <eng> --metric adoption=<value>
  -- retrospective
       NO a retrospective captured as a case: none: fde retro

to reach adoption: an adoption figure measured in the field -- none: fde outcome <eng> --metric adoption=<value>
```

## What the record knows, and who said it

Every fact carries its source. A fact learned from a person or inferred is asserted, not established; the gates below say which ones still need establishing.

```text
known (24)
  functional scope:
    external_systems = 1   [platform lead, admin]
    input_format = text   [system]
    output_shape = decision   [system]
    query_pattern = lookup   [head of support, sponsor]
    recall_span = within_turn   [platform lead, admin]
  non-functional scope:
    access_model = role_based   [platform lead, admin]
    availability_target = business_hours   [platform lead, admin]
    human_waiting = no   [system]
    interpretability_required = True   [head of support, sponsor]
    latency_budget_ms = 5000   [head of support, sponsor]
  data scope:
    arrival_rate = 500   [platform lead, admin]
    corpus_size = 13083   [platform lead, admin]
    data_residency = cannot_leave   [platform lead, admin]
    labelled_count = 9999   [platform lead, admin]
    sensitivity_present = True   [platform lead, admin]
  environment:
    accelerator = none   [platform lead, admin]
    container_competence = False   [platform lead, admin]
    environment_lifetime = permanent   [platform lead, admin]
    existing_cluster = False   [platform lead, admin]
    existing_iac_tool = none   [system]
    hosting = customer-vpc   [platform lead, admin]
    provisioning_api = True   [system]
  operations:
    operates_after_handover = platform_team   [platform lead, admin]
  commercial:
    licence_posture = internal_only   [platform lead, admin]
  still open -- data scope: corpus_churn · non-functional scope: cheap_path_coverage, confidence_calibrated

91% of what gets decided is settled

waived (2)
  client_readiness: the support lead is named as eval owner and will grade the acceptance sample; interview scheduled
  outcome_contract: the brief names the number (median time to first substantive reply, 26 hours, stated by the support lead) but nobody at the bank has set a target, and there is no bank: this is a public demonstration on the vendor's dataset

nobody has spoken for: eval_owner
```

## The number this system exists to move

No outcome contract is on the record; it is the eighth gate.

`fde outcome-contract` records the owner, the metric, its value today, the target, the method and the window -- or a waiver saying why not yet.

## The design, with its reasons

What `fde architect` decides from the facts above, with the approach each component takes and why; what could not be decided is listed under the risks. A build writes this same page as ARCHITECTURE.md.

Topology: **customer-vpc**  
Fingerprint: `2b227670cc7c1696`

### Scope

**Functional scope**
- `external_systems` = 1
- `input_format` = text
- `output_shape` = decision
- `query_pattern` = lookup
- `recall_span` = within_turn

**Non-functional scope**
- `access_model` = role_based
- `availability_target` = business_hours
- `human_waiting` = no
- `interpretability_required` = True
- `latency_budget_ms` = 5000

**Data scope**
- `arrival_rate` = 500
- `corpus_size` = 13083
- `data_residency` = cannot_leave
- `labelled_count` = 9999
- `sensitivity_present` = True

**Environment**
- `accelerator` = none
- `container_competence` = False
- `environment_lifetime` = permanent
- `existing_cluster` = False
- `existing_iac_tool` = none
- `hosting` = customer-vpc
- `provisioning_api` = True

**Operations**
- `operates_after_handover` = platform_team

**Commercial**
- `licence_posture` = internal_only

### Decisions

| Component | Approach | Implemented with | Why |
|---|---|---|---|
| accountability | decision-log (advisory: decided and emitted, not a payload step) | plain-python | Decision log: interpretability_required == true |
| deployment | systemd-unit (advisory: decided and emitted, not a payload step) | plain-python | Service unit: always |
| evaluation | labelled-metrics (advisory: decided and emitted, not a payload step) | plain-python | Labelled metrics: output_shape == decision |
| governance | role-scoped-authority (advisory: decided and emitted, not a payload step) | plain-python | Role-scoped authority: access_model == role_based |
| integration | direct-call | plain-python | Direct call: external_systems < 2 |
| observability | structured-logs (advisory: decided and emitted, not a payload step) | plain-python | Structured logs: always |
| perception | text-extraction | plain-python | Text extraction: input_format == text |
| planning | fixed-sequence | plain-python | Fixed sequence: always |
| provisioning | terraform-module (advisory: decided and emitted, not a payload step) | plain-python | Declarative provisioning: provisioning_api == true |
| reasoning | labelled-decision | plain-python | Labelled decision from text: output_shape == decision and input_format == text |
| representation | deterministic | plain-python | Deterministic: output_shape == decision |

The tool boundary is emitted UNWIRED: no external system's tools are registered and the approval gate and critic are constructed without `approve=`/`review=`. Until the implementation registers tools and wires both, every action-shaped request is refused (409) -- fail closed, by design.

### Tools and libraries

| Component | Chosen | Licence | Alternatives in this topology |
|---|---|---|---|
| accountability | plain-python | PSF | -- |
| deployment | plain-python | PSF | -- |
| evaluation | plain-python | PSF | xgboost |
| governance | plain-python | PSF | -- |
| integration | plain-python | PSF | -- |
| observability | plain-python | PSF | -- |
| perception | plain-python | PSF | -- |
| planning | plain-python | PSF | -- |
| provisioning | plain-python | PSF | -- |
| reasoning | plain-python | PSF | -- |
| representation | plain-python | PSF | -- |

Adopting an alternative the client already operates: `fde reuse <engagement> <stack>` and rebuild -- the architecture does not change, only the emitted code does.

### Agent and tool posture

- `integration` acts on the world. In front of it: approve-integration, critic-integration; an idempotency key derived from each action and reserved in the ledger (app/ledger.py) before it runs, so a retry cannot act twice.
- Access is role-scoped: the approval gate refuses an approval that names no approver role, and the audit records the role beside the person. The role names are client content.
- Tool boundary realized via `plain-python`.


### Rejected alternatives

What this design is not, and why. Usually the more useful half.

**accountability**
- `explainability-record` -- decision-log is simpler and applies here

**deployment**
- `compose` -- ruled out by container_competence == false
- `kubernetes-manifests` -- ruled out by container_competence == false and existing_cluster == false

**evaluation**
- `field-match` -- nothing here matches output_shape == structured
- `judged` -- nothing here matches output_shape == freeform

**governance**
- `audit-only` -- ruled out by access_model == role_based
- `boundary-and-audit` -- ruled out by access_model == role_based

**integration**
- `governed-tools` -- ruled out by external_systems < 2

**observability**
- `traced` -- ruled out by external_systems < 2

**perception**
- `ocr-pipeline` -- ruled out by input_format == text
- `passthrough` -- nothing here matches input_format == structured_data
- `speech-transcription` -- ruled out by input_format == text
- `video-ingestion` -- ruled out by input_format == text
- `windowed-ingestion` -- nothing here matches input_format == streams

**planning**
- `model-planner` -- ruled out by interpretability_required == true
- `optimisation` -- ruled out by input_format == text

**provisioning**
- `ansible-playbook` -- nothing here matches existing_iac_tool == ansible or provisioning_api == false
- `gitops` -- ruled out by existing_cluster == false
- `manual-runbook` -- terraform-module is simpler and applies here

**reasoning**
- `cascade` -- ruled out by interpretability_required == true
- `classical-ml` -- ruled out by input_format == text
- `finetune` -- ruled out by output_shape == decision
- `llm` -- ruled out by output_shape == decision
- `optimisation-reasoning` -- ruled out by output_shape == decision and labelled_count >= 1000

**representation**
- `assisted-deterministic` -- nothing here matches output_shape == structured and cheap_path_coverage < 0.95 and interpretability_required == true or output_shape == decision and cheap_path_coverage < 0.95 -- unanswered: cheap_path_coverage (an answer could admit it)
- `cascade` -- ruled out by interpretability_required == true
- `classical-ml` -- ruled out by input_format == text
- `finetune` -- ruled out by output_shape == decision
- `llm-extraction` -- ruled out by interpretability_required == true
- `segmentation` -- nothing here matches output_shape == freeform

### Licences

Everything this design pulls in, so it can be checked before a legal team checks it.

- `plain-python`: PSF

## What the design rests on, and what was accepted

Waived gates, overridden recommendations, assumptions nobody has answered, and the facts the governance follows from. A build writes this same page as RISKS.md.

### Decided, emitted, not on the payload path

These components were decided and their modules are emitted, but the request path does not run them: the edge's structured log is the observability that runs, the ledger is the audit that runs, the unit is the deployment. Each module says so in its first lines. Wire one in, or leave it as the reference it is -- but do not read its presence as running code.

- `accountability`
- `deployment`
- `evaluation`
- `governance`
- `observability`
- `provisioning`

### Identity at the edge

One bearer token, one service principal, one set of scopes: every caller acts as the same identity, so the audit names the service, not a person. Per-caller identity is an `access_model` decision nobody has answered; accept this or front the service with something that does.

### Facts this design stands on

The governance, the boundary and the topology follow from these values. A value learned from a person or inferred is asserted, not established -- confirm it with the client before the decision that rests on it stands.

- `data_residency = cannot_leave` -- interview -- asserted, not established: confirm before the decisions resting on it stand
- `hosting = customer-vpc` -- interview -- asserted, not established: confirm before the decisions resting on it stand

### Unanswered assumptions

Decisions were made without these facts. Each is a risk until somebody answers it (`fde ask`, or the interview), and the answer may change a decision.

- cheap_path_coverage: not stated, so nothing was decided on it
- confidence_calibrated: not stated, so nothing was decided on it
- corpus_churn: not stated, so nothing was decided on it

### Gates waived

Each was blocking at build time. Somebody decided to proceed anyway, and this is who said what.

- **client_readiness** (2026-09-19) -- the support lead is named as eval owner and will grade the acceptance sample; interview scheduled
  - covered: Nobody has been named who can say what separates acceptable from excellent.
- **outcome_contract** (2026-09-20) -- the brief names the number (median time to first substantive reply, 26 hours, stated by the support lead) but nobody at the bank has set a target, and there is no bank: this is a public demonstration on the vendor's dataset
  - covered: Nobody has agreed which number this system exists to move: no outcome contract was recorded.

## Decision debt

Everything the engagement rests on that nobody has settled, each with an owner and an age.

```text
banking: decision debt as of 2026-10-12

  open (12)
    waiver         client_readiness: the support lead is named as eval owner and will grade the acceptance sample; interview scheduled
                   owner: eval_owner  23 day(s)
                   next: meet the gate, or restate the waiver if it still holds
    waiver         outcome_contract: the brief names the number (median time to first substantive reply, 26 hours, stated by the support lead) but nobody at the bank has set a target, and there is no bank: this is a public demonstration on the vendor's dataset
                   owner: the author  22 day(s)
                   next: meet the gate, or restate the waiver if it still holds
    stated         accelerator = none: said by platform lead (admin), measurable but not measured
                   owner: admin
                   next: measure it: fde scan, or a document the client owns
    stated         container_competence = False: said by platform lead (admin), measurable but not measured
                   owner: admin
                   next: measure it: fde scan, or a document the client owns
    stated         existing_cluster = False: said by platform lead (admin), measurable but not measured
                   owner: admin
                   next: measure it: fde scan, or a document the client owns
    unsigned       data_access (2026-09-19)
                   owner: unsigned  23 day(s)
                   next: re-record with --by, or leave it and know it
    unsigned       security_review (2026-09-19)
                   owner: unsigned  23 day(s)
                   next: re-record with --by, or leave it and know it
    unsigned       waiver client_readiness (2026-09-19)
                   owner: unsigned  23 day(s)
                   next: re-record with --by, or leave it and know it
    unsigned       closed inc-001 (2026-09-20)
                   owner: unsigned  22 day(s)
                   next: re-record with --by, or leave it and know it
    unheard        eval_owner has never been asked
                   owner: eval_owner
                   next: fde ask <eng> --role eval_owner
    unheard        user has never been asked
                   owner: user
                   next: fde ask <eng> --role user
    unheard        skeptic has never been asked
                   owner: skeptic
                   next: fde ask <eng> --role skeptic

12 item(s): 0 blocking the build, 0 blocking production, 0 older than 30 days, 4 unsigned
```

## What would stop this

The conditions on record under which the honest answer is to stop, judged against what has been measured so far.

```text
ok  answered_accuracy < 0.88             measured 0.902
  ok  abstain_rate > 0.25                  measured 0.182
```

## Who has been heard

Who said what, who signed what, and which roles have not been asked.

```text
banking: stakeholders

  sponsor     the author, as head of support 1 session(s), 3 fact(s) from head of support
              owns:                        success criteria, budget, political constraints
  eval_owner  --                           never heard: fde ask <eng> --role eval_owner
              owns:                        what separates excellent from acceptable
  user        --                           never heard: fde ask <eng> --role user
              owns:                        the real workflow and its exceptions
  admin       the author, as platform lead 2 session(s), 16 fact(s) from platform lead
              owns:                        data access, audit, topology, entitlements
  skeptic     --                           never heard: fde ask <eng> --role skeptic
              owns:                        why the last attempts failed

unheard: eval_owner, user, skeptic

on the record with nobody's name on it: data_access (2026-09-19); security_review (2026-09-19); waiver client_readiness (2026-09-19); closed inc-001 (2026-09-20)  (pass --by next time)
```

## The next decision

The single best next action judged from everything above, and what turns on it.

```text
next: fde implement project-0.1.27 --holdout engagements/banking/artifacts/holdout.jsonl
  built -- drive it green, then run evals/acceptance.md with the client, and fde retro after the measurement window
```
