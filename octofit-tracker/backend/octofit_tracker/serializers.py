from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField())

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField()
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()  # Duration in seconds

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
