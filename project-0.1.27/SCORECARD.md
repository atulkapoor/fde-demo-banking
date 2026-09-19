# Scorecard

**19 of 23 measured properties hold.** Measured on `/Users/atulkapoor/Documents/fde-demo-banking/project-0.1.27`. A property this build cannot measure is marked n/a, never counted as held. The service was booted on the machine that ran this card, not inside the deployed unit; the out-of-sample rows (holdout, external exam, generalisation gap, the baseline's bar) are the fitness rows, the rest are self-consistency.

| Property | Measured | Holds |
|---|---|---|
| own tests | 7 passed in 3.27s | yes |
| lint | clean | yes |
| exam: golden | 84.1% on 6946 cases (majority 1.9%; abstained 10.0%, 93.5% on the answered; in-sample: the baseline is fitted on this file) | yes |
| exam: edge_case | 47.1% on 17 cases (majority 47.1%; abstained 47.1%, 88.9% on the answered) | **no** |
| exam: adversarial | 90.9% on 11 cases (0 followed, 0 on misread bases) | **no** |
| exam: verdict | the attack layer found takers -- 0 injection(s) followed, 0 answered wrong regardless of the injection (the base case is misread un-steered), 1 answered wrong u | **no** |
| exam record | every eval file matches its recorded digest | yes |
| holdout | 73.7% on 3036 cases (majority 1.9%; abstained 16.1%, 87.9% on the answered) | yes |
| holdout: sample size | 3036 cases | yes |
| holdout: the file on record | matches evals/manifest.json | yes |
| generalisation gap | golden 84.1% - holdout 73.7% = +10.4% | yes |
| beats the baseline error rate | 87.9% on the answered against a recorded first-pass accuracy of 88.0%, abstaining 16.1% | **no** |
| external exam | 72.2% on 3079 cases (majority 1.3%) | yes |
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
| regression from the last card | no previous card | n/a |

## Not holding

- **exam: edge_case**: 47.1% on 17 cases (majority 47.1%; abstained 47.1%, 88.9% on the answered)
- **exam: adversarial**: 90.9% on 11 cases (0 followed, 0 on misread bases)
- **exam: verdict**: the attack layer found takers -- 0 injection(s) followed, 0 answered wrong regardless of the injection (the base case is misread un-steered), 1 answered wrong u -- the harness's own exit status at --min-score 0.0
- **beats the baseline error rate**: 87.9% on the answered against a recorded first-pass accuracy of 88.0%, abstaining 16.1% -- evals/acceptance.md: the baseline's error rate is the number to beat; measured on what the system answered, with the abstained share beside it

## Notes

- own tests: the deliverable's own smoke and edge tests, model-free
- holdout: cases the delivery never shipped; the harness's holdout floor applies
- holdout: sample size: the protocol's floor for a blind sample is 30; the acceptance run itself is sized to the golden set
- generalisation gap: past 20% the golden score describes the exam, not the system; a component that reads the holdout file defeats this row, which is what --external is for
- edge: identity: no token, no service, with a request id
- edge: forged result: a caller cannot hand the pipeline its own answer
- edge: a valid request: the exam's own first case through the edge; refusals alone proved a service that failed every real request
- edge: the answer says why: an answer names what it stood on: scores and carrying tokens, cited evidence, or who decided
- edge: readiness: judged where nothing external is needed; with a model seam it depends on the deployment's endpoint and is reported only
- risk register: scaffolds: a scaffold raises on use; a green exam cannot include it
- risk register: gates waived: reported, not judged: a waiver is the engagement's decision, on the record
- risk register: asserted facts: reported: confirm each with the client before the decisions resting on it stand
