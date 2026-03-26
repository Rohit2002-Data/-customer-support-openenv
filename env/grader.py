
from .policy import check_policy

def apply_penalty(score, violations):
    return score - 0.3 * len(violations)

def grade(action, task, steps):
    score = 0.0

    if action.category == task["expected_category"]:
        score += 0.4

    if action.action_type == task["expected_action"]:
        score += 0.3

    if action.response_text and len(action.response_text) > 20:
        score += 0.2

    if steps <= 2:
        score += 0.1
    else:
        score -= 0.2

    violations = check_policy(action, action.category or "")
    score = apply_penalty(score, violations)

    return max(0.0, min(1.0, score)), str(violations)
