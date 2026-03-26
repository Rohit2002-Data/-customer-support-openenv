
POLICIES = {
    "security": ["Always escalate security issues"],
    "billing": ["Mention refund if duplicate charge"],
    "account": ["Guide reset steps"]
}

def check_policy(action, category):
    violations = []

    if category == "security" and action.action_type != "escalate":
        violations.append("Security issue not escalated")

    if action.response_text:
        if "password" in action.response_text.lower() and "reset" not in action.response_text.lower():
            violations.append("Unsafe password handling")

    return violations
