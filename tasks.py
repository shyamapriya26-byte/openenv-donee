# tasks.py
TASKS = [
    {
        "name": "internet_not_working",
        "difficulty": "easy",
        "grader": "grader.grade_internet_not_working",
        "description": "User reports no internet connection."
    },
    {
        "name": "slow_laptop",
        "difficulty": "medium",
        "grader": "grader.grade_slow_laptop",
        "description": "Laptop is running very slowly."
    },
    {
        "name": "wifi_disconnecting",
        "difficulty": "hard",
        "grader": "grader.grade_wifi_disconnecting",
        "description": "Wi-Fi keeps disconnecting."
    }
]

# These are for env.py (renamed to avoid conflict with TASKS above)
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
