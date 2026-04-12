# tasks.py
from grader import (
    grade_internet_not_working,
    grade_slow_laptop,
    grade_wifi_disconnecting,
    grade_action      # keep this so env.py can import it
)

# ========== KEEP YOUR ORIGINAL DICTIONARIES ==========
TASKS = {
    "easy": ["internet not working"],
    "medium": ["slow laptop"],
    "hard": ["wifi disconnecting", "battery draining fast"]
}

ISSUES = {
    "internet not working": [
        ["ask_issue", "suggest_restart", "confirm_fix"],
        ["ask_issue", "check_cables", "confirm_fix"]
    ],
    "slow laptop": [
        ["ask_issue", "suggest_cleanup", "confirm_fix"]
    ],
    "wifi disconnecting": [
        ["ask_issue", "suggest_reconnect", "confirm_fix"]
    ],
    "battery draining fast": [
        ["ask_issue", "suggest_close_apps", "confirm_fix"]
    ]
}

# ========== ADD THIS FOR VALIDATION ==========
tasks = [
    {
        "name": "internet not working",
        "difficulty": "easy",
        "grader": grade_internet_not_working,
        "description": "User reports no internet connection."
    },
    {
        "name": "slow laptop",
        "difficulty": "medium",
        "grader": grade_slow_laptop,
        "description": "Laptop is running very slowly."
    },
    {
        "name": "wifi disconnecting",
        "difficulty": "hard",
        "grader": grade_wifi_disconnecting,
        "description": "Wi-Fi keeps disconnecting."
    }
]
