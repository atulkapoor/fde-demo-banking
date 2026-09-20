# Architecture

Topology: **customer-vpc**  
Fingerprint: `2b227670cc7c1696`

## Scope

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

## Decisions

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

## Tools and libraries

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

## Agent and tool posture

- `integration` acts on the world. In front of it: approve-integration, critic-integration; an idempotency key derived from each action and reserved in the ledger (app/ledger.py) before it runs, so a retry cannot act twice.
- Access is role-scoped: the approval gate refuses an approval that names no approver role, and the audit records the role beside the person. The role names are client content.
- Tool boundary realized via `plain-python`.


## Rejected alternatives

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

## Assumptions

Nobody answered these, so nothing was decided on them. Each is a question worth asking before this is built.

- cheap_path_coverage: not stated, so nothing was decided on it
- confidence_calibrated: not stated, so nothing was decided on it
- corpus_churn: not stated, so nothing was decided on it

## Licences

Everything this design pulls in, so it can be checked before a legal team checks it.

- `plain-python`: PSF
