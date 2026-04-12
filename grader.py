# grader.py
def grade_action(action, correct_action):
    if action == correct_action:
        return 1.0
    elif action.startswith("suggest") and correct_action.startswith("suggest"):
        return 0.5
    else:
        return 0.0

def grade_internet_not_working(sample, item=None):
    if not isinstance(sample, list):
        return 0.0
    perfect_paths = [
        ["ask_issue", "suggest_restart", "confirm_fix"],
        ["ask_issue", "check_cables", "confirm_fix"]
    ]
    if sample in perfect_paths:
        return 1.0
    if sample and sample[-1] == "confirm_fix":
        return 0.5
    return 0.0

def grade_slow_laptop(sample, item=None):
    if not isinstance(sample, list):
        return 0.0
    perfect_path = ["ask_issue", "suggest_cleanup", "confirm_fix"]
    if sample == perfect_path:
        return 1.0
    if sample and sample[-1] == "confirm_fix":
        return 0.5
    return 0.0

def grade_wifi_disconnecting(sample, item=None):
    if not isinstance(sample, list):
        return 0.0
    perfect_path = ["ask_issue", "suggest_reconnect", "confirm_fix"]
    if sample == perfect_path:
        return 1.0
    if sample and sample[-1] == "confirm_fix":
        return 0.5
    return 0.0
