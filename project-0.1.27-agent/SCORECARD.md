# Scorecard

**22 of 24 measured properties hold.** Measured on `/Users/atulkapoor/Documents/fde-demo-banking/project-0.1.27-agent`. A property this build cannot measure is marked n/a, never counted as held. The service was booted on the machine that ran this card, not inside the deployed unit; the out-of-sample rows (holdout, external exam, generalisation gap, the baseline's bar) are the fitness rows, the rest are self-consistency.

| Property | Measured | Holds |
|---|---|---|
| own tests | 7 passed in 3.46s | yes |
| lint | clean | yes |
| exam: golden | 89.2% on 6946 cases (majority 1.9%; abstained 8.4%, 97.3% on the answered; in-sample: the baseline is fitted on this file) | yes |
| exam: edge_case | 47.1% on 17 cases (majority 47.1%; abstained 47.1%, 88.9% on the answered) | **no** |
| exam: adversarial | 100.0% on 11 cases (0 followed, 0 on misread bases) | yes |
| exam: verdict | green | yes |
| exam record | every eval file matches its recorded digest | yes |
| holdout | 73.8% on 3036 cases (majority 1.9%; abstained 18.2%, 90.2% on the answered) | yes |
| holdout: sample size | 3036 cases | yes |
| holdout: the file on record | matches evals/manifest.json | yes |
| generalisation gap | golden 89.2% - holdout 73.8% = +15.4% | yes |
| beats the baseline error rate | 90.2% on the answered against a recorded first-pass accuracy of 88.0%, abstaining 18.2% | yes |
| external exam | 71.6% on 3079 cases (majority 1.3%) | yes |
| edge: boots | answers /health | yes |
| edge: identity | 401 without a token | yes |
| edge: forged result | 422 | yes |
| edge: forged identity | 422 | yes |
| edge: malformed body | 400 | yes |
| edge: a valid request | 200 "card_arrival" | yes |
| edge: the answer says why | yes | yes |
| edge: readiness | 200 ready | yes |
| risk register: scaffolds | none | yes |
| risk register: gates waived | client_readiness | n/a |
| risk register: asserted facts | 2 boundary-bearing fact(s) asserted | n/a |
| environment | every variable the code reads is documented | yes |
| training path | none in this build | n/a |
| regression from the last card | exam: golden 91.6% -> 89.2%; holdout 77.5% -> 73.8% | **no** |

## Not holding

- **exam: edge_case**: 47.1% on 17 cases (majority 47.1%; abstained 47.1%, 88.9% on the answered)
- **regression from the last card**: exam: golden 91.6% -> 89.2%; holdout 77.5% -> 73.8% -- tolerance 2%

## Notes

- own tests: the deliverable's own smoke and edge tests, model-free
- exam: verdict: the harness's own exit status at --min-score 0.0
- holdout: cases the delivery never shipped; the harness's holdout floor applies
- holdout: sample size: the protocol's floor for a blind sample is 30; the acceptance run itself is sized to the golden set
- generalisation gap: past 20% the golden score describes the exam, not the system; a component that reads the holdout file defeats this row, which is what --external is for
- beats the baseline error rate: evals/acceptance.md: the baseline's error rate is the number to beat; measured on what the system answered, with the abstained share beside it
- edge: identity: no token, no service, with a request id
- edge: forged result: a caller cannot hand the pipeline its own answer
- edge: a valid request: the exam's own first case through the edge; refusals alone proved a service that failed every real request
- edge: the answer says why: an answer names what it stood on: scores and carrying tokens, cited evidence, or who decided
- edge: readiness: judged where nothing external is needed; with a model seam it depends on the deployment's endpoint and is reported only
- risk register: scaffolds: a scaffold raises on use; a green exam cannot include it
- risk register: gates waived: reported, not judged: a waiver is the engagement's decision, on the record
- risk register: asserted facts: reported: confirm each with the client before the decisions resting on it stand
