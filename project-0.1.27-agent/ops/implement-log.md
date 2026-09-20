# Implementation log

## Round 1

- check: red
- changed: app/components/reasoning.py

```
               - {"id": "q-01795", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "card_payment_not_recognised"}
               - {"id": "q-01796", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "direct_debit_payment_not_recognised"}
               - {"id": "q-01798", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "unknown"}
  adversarial    11 cases  90.9%
               by source: {'output': 1}
               majority rate 42.9%, macro-F1 0.700
               abstained 14.3%; accuracy on the answered 100.0%
                 balance_not_updated_after_cheque_or_cash P 1.00  R 1.00  F1 1.00  n=1
                 card_payment_fee_charged                 P 1.00  R 1.00  F1 1.00  n=3
                 direct_debit_payment_not_recognised      P 1.00  R 0.67  F1 0.80  n=3
                 unknown                                  P 0.00  R 0.00  F1 0.00  n=0
               confusion: {'direct_debit_payment_not_recognised -> unknown': 1}
               - {"id": "adv-injection-steered", "source": "output", "missed": [], "invented": [], "expected": "direct_debit_payment_not_recognised", "got": "unknown", "kind": "
{"level": "warning", "ledger": "STATE_DIR unset: audit and idempotency live in process memory and vanish on restart"}
below 88.0%
```

## Round 2

- check: green

```
               confusion: {'contactless_not_working -> unknown': 2, 'contactless_not_working -> card_payment_not_recognised': 2, 'top_up_limits -> unknown': 1, 'contactless_not_working -> declined_cash_withdrawal': 1, 'contactless_not_working -> direct_debit_payment_not_recognised': 1, 'contactless_not_working -> pending_transfer': 1}
               - {"id": "q-02294", "source": "output", "missed": [], "invented": [], "expected": "top_up_limits", "got": "unknown"}
               - {"id": "q-01782", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "unknown"}
               - {"id": "q-01784", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "unknown"}
               - {"id": "q-01790", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "declined_cash_withdrawal"}
               - {"id": "q-01793", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "card_payment_not_recognised"}
               - {"id": "q-01795", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "card_payment_not_recognised"}
               - {"id": "q-01796", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "direct_debit_payment_not_recognised"}
               - {"id": "q-01798", "source": "output", "missed": [], "invented": [], "expected": "contactless_not_working", "got": "pending_transfer"}
  adversarial    11 cases  100.0%
               majority rate 42.9%, macro-F1 1.000
                 balance_not_updated_after_cheque_or_cash P 1.00  R 1.00  F1 1.00  n=1
                 card_payment_fee_charged                 P 1.00  R 1.00  F1 1.00  n=3
                 direct_debit_payment_not_recognised      P 1.00  R 1.00  F1 1.00  n=3
{"level": "warning", "ledger": "STATE_DIR unset: audit and idempotency live in process memory and vanish on restart"}
holdout: green (cases the implementer never saw) -- 77.5% (shipped baseline 73.7%) -- the file the build recorded
```

**Stopped by**: harness green.
