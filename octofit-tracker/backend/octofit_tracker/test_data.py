from datetime import timedelta

def get_test_data():
    return {
        "users": [
            {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ],
        "teams": [
            {"name": "Blue Team", "members": ["thundergod", "metalgeek"]},
            {"name": "Gold Team", "members": ["zerocool", "crashoverride", "sleeptoken"]},
        ],
        "activities": [
            {"user": "thundergod", "activity_type": "Cycling", "duration": int(timedelta(hours=1).total_seconds())},
            {"user": "metalgeek", "activity_type": "Crossfit", "duration": int(timedelta(hours=2).total_seconds())},
            {"user": "zerocool", "activity_type": "Running", "duration": int(timedelta(hours=1, minutes=30).total_seconds())},
            {"user": "crashoverride", "activity_type": "Strength", "duration": int(timedelta(minutes=30).total_seconds())},
            {"user": "sleeptoken", "activity_type": "Swimming", "duration": int(timedelta(hours=1, minutes=15).total_seconds())},
        ],
        "leaderboard": [
            {"user": "thundergod", "score": 100},
            {"user": "metalgeek", "score": 90},
            {"user": "zerocool", "score": 95},
            {"user": "crashoverride", "score": 85},
            {"user": "sleeptoken", "score": 80},
        ],
        "workouts": [
            {"name": "Cycling Training", "description": "Training for a road cycling event"},
            {"name": "Crossfit", "description": "Training for a crossfit competition"},
            {"name": "Running Training", "description": "Training for a marathon"},
            {"name": "Strength Training", "description": "Training for strength"},
            {"name": "Swimming Training", "description": "Training for a swimming competition"},
        ],
    }
