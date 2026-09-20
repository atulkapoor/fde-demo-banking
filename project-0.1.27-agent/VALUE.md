# Value

What the measured system is worth to `banking`, in the client's own figures. Every line says what it rests on: **measured** by the exam or the baseline, **stated** by the client and not measured, **assumed** by the caller of this estimate, or **derived** from the lines above it. Argue the rows, not the total.

| Line | Value | Unit | Basis | Note |
|---|---|---|---|---|
| annual volume | 120000 | items/year | stated | from 10000.0 messages/month |
| human hours today | 1500 | hours/year | stated | 45 s per item, stated cycle time |
| labour on record | 1440 | hours/year | stated | 30.0 h/week x 48 weeks; the cycle-time figure above is the one used |
| hourly cost | 30.0 | per hour | assumed | supplied by the caller |
| cost of the work today | 45000 | per year | derived |  |
| automated share | 0.818 | of items | measured | 1 - the holdout's abstain rate (18.2%) on 3036 cases never shipped |
| accuracy on the automated | 0.902 |  | measured | the holdout's accuracy on what the system answered |
| human review of automated items | 0.2 | share | assumed | supplied by the caller: a person checks this share of automated decisions |
| residual human share | 0.346 | of items | derived | abstained items plus the reviewed share |
| hours saved | 982 | hours/year | derived |  |
| saving | 29448 | per year | derived |  |
| errors the system makes on the automated | 9620 | items/year | measured | 9.8% of the automated items |
| errors a person made on the same items | 11779 | items/year | stated | 12.0% first-pass error rate on the baseline |
| net errors | -2160 | items/year | derived | positive means the system adds errors; the cost of one is the client's figure to supply |
| cost to build | 4800 | one-off | assumed | 160.0 hours at the hourly cost |
| cost to run | 3600 | per year | assumed | 300.0 per month, supplied by the caller |
| net benefit | 25848 | per year | derived | saving minus the cost to run |
| payback | 2.2 | months | derived |  |
| accuracy interval | 89.0% to 91.3% | 95% | derived | Wilson interval on 2483 answered holdout cases |

Stated, not measured: annual volume, human hours today, labour on record, errors a person made on the same items. Measure these before quoting the total.
Assumed by the caller: hourly cost, human review of automated items, cost to build, cost to run.
