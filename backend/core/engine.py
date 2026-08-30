# Policy Engine
# Validates AI-proposed actions before they are executed.


POLICY_LIMITS = {
    "discount": 20,  # Maximum discount allowed: 20%
}


def check_policy(action: str, value: float) -> dict:
    """
    Check whether an AI-proposed action is allowed by policy.
    """

    if action == "discount":
        maximum = POLICY_LIMITS["discount"]

        if value > maximum:
            return {
                "allowed": False,
                "action": action,
                "value": value,
                "reason": f"Discount exceeds maximum allowed limit of {maximum}%",
            }

        return {
            "allowed": True,
            "action": action,
            "value": value,
            "reason": "Action complies with policy",
        }

    return {
        "allowed": False,
        "action": action,
        "value": value,
        "reason": "Action is not approved by policy",
    }