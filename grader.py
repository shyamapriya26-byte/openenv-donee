# grader.py

def grade_internet_not_working(sample, item=None):
    """
    Grader for 'internet not working' (easy task).
    Returns 1.0 for perfect solution, 0.5 for partial, 0.0 otherwise.
    """
    if not isinstance(sample, list):
        return 0.0
    
    perfect_paths = [
        ["ask_issue", "suggest_restart", "confirm_fix"],
        ["ask_issue", "check_cables", "confirm_fix"]
    ]
    if sample in perfect_paths:
        return 1.0
    
    # Partial credit: last action is confirm_fix (agent tried to resolve)
    if sample and sample[-1] == "confirm_fix":
        return 0.5
    return 0.0


def grade_slow_laptop(sample, item=None):
    """
    Grader for 'slow laptop' (medium task).
    """
    if not isinstance(sample, list):
        return 0.0
    
    perfect_path = ["ask_issue", "suggest_cleanup", "confirm_fix"]
    if sample == perfect_path:
        return 1.0
    
    # Partial credit: last action is confirm_fix
    if sample and sample[-1] == "confirm_fix":
        return 0.5
    return 0.0


def grade_wifi_disconnecting(sample, item=None):
    """
    Grader for 'wifi disconnecting' (hard task).
    """
    if not isinstance(sample, list):
        return 0.0
    
    perfect_path = ["ask_issue", "suggest_reconnect", "confirm_fix"]
    if sample == perfect_path:
        return 1.0
    
    # Partial credit: last action is confirm_fix
    if sample and sample[-1] == "confirm_fix":
        return 0.5
    return 0.0
