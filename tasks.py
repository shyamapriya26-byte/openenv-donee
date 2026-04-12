# tasks.py
from grader import (
    grade_internet_not_working,
    grade_slow_laptop,
    grade_wifi_disconnecting
)

# Required variable name for OpenEnv validation
tasks = [
    {
        "name": "internet not working",
        "difficulty": "easy",
        "grader": grade_internet_not_working,
        "description": "User reports no internet connection. Diagnose and fix."
    },
    {
        "name": "slow laptop",
        "difficulty": "medium",
        "grader": grade_slow_laptop,
        "description": "Laptop is running very slowly. Find and apply solution."
    },
    {
        "name": "wifi disconnecting",
        "difficulty": "hard",
        "grader": grade_wifi_disconnecting,
        "description": "Wi-Fi keeps disconnecting every few minutes. Resolve issue."
    }
]
