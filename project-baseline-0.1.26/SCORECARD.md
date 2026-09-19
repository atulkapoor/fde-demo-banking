# Scorecard

**16 of 17 measured properties hold.** Measured on `/Users/atulkapoor/Documents/fde-demo-banking/project`. A property this build cannot measure is marked n/a, never counted as held.

| Property | Measured | Holds |
|---|---|---|
| own tests | 6 passed in 3.50s | yes |
| lint | clean | yes |
| exam: golden | 87.0% on 6946 cases (majority 1.9%; in-sample: the baseline is fitted on this file) | yes |
| exam: edge_case | 47.1% on 17 cases (majority 47.1%) | **no** |
| exam: adversarial | 100.0% on 11 cases (0 followed, 0 on misread bases) | yes |
| exam: verdict | green | yes |
| holdout | 78.5% on 3036 cases (majority 1.9%) | yes |
| holdout: sample size | 3036 cases | yes |
| holdout: the file on record | matches evals/manifest.json | yes |
| exam record | every eval file matches its recorded digest | yes |
| edge: boots | answers /health | yes |
| edge: identity | 401 without a token | yes |
| edge: forged result | 422 | yes |
| edge: forged identity | 422 | yes |
| edge: malformed body | 400 | yes |
| edge: readiness | 200 ready | n/a |
| risk register: scaffolds | none | yes |
| risk register: gates waived | client_readiness | n/a |
| risk register: asserted facts | 3 boundary-bearing fact(s) asserted | n/a |
| environment | every variable the code reads is documented | yes |
| training path | none in this build | n/a |

## Not holding

- **exam: edge_case**: 47.1% on 17 cases (majority 47.1%)

## Notes

- own tests: the deliverable's own smoke and edge tests, model-free
- exam: verdict: the harness's own exit status at --min-score 0.0
- holdout: cases the delivery never shipped; the harness's holdout floor applies
- holdout: sample size: the acceptance protocol's floor is 30
- edge: identity: no token, no service, with a request id
- edge: forged result: a caller cannot hand the pipeline its own answer
- edge: readiness: reported, not judged: readiness depends on the deployment's model and corpus
- risk register: scaffolds: a scaffold raises on use; a green exam cannot include it
- risk register: gates waived: reported, not judged: a waiver is the engagement's decision, on the record
- risk register: asserted facts: reported: confirm each with the client before the decisions resting on it stand
