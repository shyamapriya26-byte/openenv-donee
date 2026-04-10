# tasks.py

from grader import (
    grade_internet_not_working,
    grade_slow_laptop,
    grade_wifi_disconnecting,
    grade_battery_draining_fast
)

# ========== TASKS WITH EMBEDDED GRADERS ==========
# Each task is a dictionary with "name" and "grader" fields.
# This structure is required by the validation system.

TASKS = {
    "easy": [
        {"name": "internet not working", "grader": grade_internet_not_working}
    ],
    "medium": [
        {"name": "slow laptop", "grader": grade_slow_laptop}
    ],
    "hard": [
        {"name": "wifi disconnecting", "grader": grade_wifi_disconnecting},
        {"name": "battery draining fast", "grader": grade_battery_draining_fast}
    ]
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
