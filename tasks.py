# tasks.py
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

TASKS = [
    {
        "name": "internet_not_working",
        "difficulty": "easy",
        "grader": grade_internet_not_working,
        "description": "User reports no internet connection."
    },
    {
        "name": "slow_laptop",
        "difficulty": "medium",
        "grader": grade_slow_laptop,
        "description": "Laptop is running very slowly."
    },
    {
        "name": "wifi_disconnecting",
        "difficulty": "hard",
        "grader": grade_wifi_disconnecting,
        "description": "Wi-Fi keeps disconnecting."
    }
]

# For your env.py
TASK_DIFFICULTY_MAP = {
    "easy": ["internet_not_working"],
    "medium": ["slow_laptop"],
    "hard": ["wifi_disconnecting", "battery_draining_fast"]
}

ISSUES = {
    "internet_not_working": [
        ["ask_issue", "suggest_restart", "confirm_fix"],
        ["ask_issue", "check_cables", "confirm_fix"]
    ],
    "slow_laptop": [
        ["ask_issue", "suggest_cleanup", "confirm_fix"]
    ],
    "wifi_disconnecting": [
        ["ask_issue", "suggest_reconnect", "confirm_fix"]
    ],
    "battery_draining_fast": [
        ["ask_issue", "suggest_close_apps", "confirm_fix"]
    ]
}
