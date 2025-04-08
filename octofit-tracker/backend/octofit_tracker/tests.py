from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User(username='testuser', email='testuser@example.com', password='password123').save()
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        user1 = User(username='user1', email='user1@example.com', password='password123').save()
        user2 = User(username='user2', email='user2@example.com', password='password123').save()
        team = Team(name='Test Team', members=[user1, user2]).save()
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User(username='testuser', email='testuser@example.com', password='password123').save()
        activity = Activity(user=user, activity_type='Running', duration=3600).save()
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User(username='testuser', email='testuser@example.com', password='password123').save()
        leaderboard = Leaderboard(user=user, score=100).save()
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout(name='Test Workout', description='Test Description').save()
        self.assertEqual(workout.name, 'Test Workout')
