# Advisory: decided and recorded at build time -- not a
# step the payload passes through; the pipeline does not
# chain this module.
"""governance: role-scoped-authority, via plain-python.

Role-scoped authority: access_model == role_based

Approval and audit that know which role is speaking. Two contracts, both
refused rather than defaulted:

**An approval names its approver role.** An approval from someone who happens
to have a login is the accountability chain lost at the first link. The gate
below raises on an approval without a role, and the roles themselves are
client content -- this module fixes the contract and refuses to invent names.

**The audit names the person, the role, and the agent.** A record saying an
agent acted has lost the chain; a record saying a person acted has hidden the
agent. Both appear, every time.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

interface = "Guard"
approach = "role-scoped-authority"
stack = "plain-python"


class UnscopedApproval(RuntimeError):
    """An approval arrived without an approver role."""


@dataclass(frozen=True)
class Approval:
    actor: str          # the person
    approver_role: str  # the role under which they approve
    action: str
    at: str


APPROVED: dict[str, Approval] = {}
AUDIT: list[dict] = []


def approve(actor: str, approver_role: str, action: str) -> Approval:
    if not (approver_role or "").strip():
        raise UnscopedApproval(
            f"approval of {action!r} by {actor!r} names no approver role -- "
            f"refused, not defaulted"
        )
    approval = Approval(actor, approver_role, action,
                        datetime.now(timezone.utc).isoformat())
    APPROVED[action] = approval
    AUDIT.append({"subject": actor, "role": approver_role, "actor": "agent",
                  "action": action, "at": approval.at})
    return approval


def require_approval(action: str) -> Approval:
    approval = APPROVED.get(action)
    if approval is None:
        raise UnscopedApproval(f"{action!r} has no recorded approval")
    return approval
