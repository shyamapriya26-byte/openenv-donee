# tasks.py

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

# ========== IMPORT GRADERS ==========
from grader import (
    grade_internet_not_working,
    grade_slow_laptop,
    grade_wifi_disconnecting
)

# ========== REGISTER TASKS WITH GRADERS ==========

# Format 1: List 
TASKS_WITH_GRADERS = [
    ("internet not working", grade_internet_not_working),
    ("slow laptop", grade_slow_laptop),
    ("wifi disconnecting", grade_wifi_disconnecting),
]

# Format 2: Dictionary 
GRADERS = {
    "internet not working": grade_internet_not_working,
    "slow laptop": grade_slow_laptop,
    "wifi disconnecting": grade_wifi_disconnecting,
}

