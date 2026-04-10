# grader.py

def grade_action(action, correct_action):
    if action == correct_action:
        return 1.0
    elif action.startswith("suggest") and correct_action.startswith("suggest"):
        return 0.5
    else:
        return 0.0

# ========== TASK-SPECIFIC GRADERS ==========
# Each grader returns a score between 0.0 and 1.0

def grade_internet_not_working(agent_actions, environment_state=None):
    """Grader for the 'internet not working' task."""
    valid_paths = [
        ["ask_issue", "suggest_restart", "confirm_fix"],
        ["ask_issue", "check_cables", "confirm_fix"]
    ]
    if agent_actions in valid_paths:
        return 1.0
    if agent_actions and agent_actions[-1] == "confirm_fix":
        return 0.5
    return 0.0

def grade_slow_laptop(agent_actions, environment_state=None):
    """Grader for the 'slow laptop' task."""
    valid_paths = [
        ["ask_issue", "suggest_cleanup", "confirm_fix"]
    ]
    return 1.0 if agent_actions in valid_paths else 0.0

def grade_wifi_disconnecting(agent_actions, environment_state=None):
    """Grader for the 'wifi disconnecting' task."""
    valid_paths = [
        ["ask_issue", "suggest_reconnect", "confirm_fix"]
    ]
    return 1.0 if agent_actions in valid_paths else 0.0

def grade_battery_draining_fast(agent_actions, environment_state=None):
    """Grader for the 'battery draining fast' task."""
    valid_paths = [
        ["ask_issue", "suggest_close_apps", "confirm_fix"]
    ]
    return 1.0 if agent_actions in valid_paths else 0.0
