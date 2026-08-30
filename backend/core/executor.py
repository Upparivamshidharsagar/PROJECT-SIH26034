from backend.core.engine import check_policy


def execute_action(action: str, value: float) -> dict:
    """
    Execute an action only if it passes the Policy Engine.
    """

    policy_result = check_policy(action, value)

    if not policy_result["allowed"]:
        return {
            "executed": False,
            "action": action,
            "value": value,
            "reason": policy_result["reason"],
        }

    return {
        "executed": True,
        "action": action,
        "value": value,
        "reason": "Action executed successfully",
    }