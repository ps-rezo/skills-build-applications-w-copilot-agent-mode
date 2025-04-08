from django.core.management.base import BaseCommand
from mongoengine import connect
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        connect(db="octofit_db", host="localhost", port=27017)

        # Clear existing data
        User.objects.delete()
        Team.objects.delete()
        Activity.objects.delete()
        Leaderboard.objects.delete()
        Workout.objects.delete()

        # Create users
        users = [
            User(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword').save(),
            User(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword').save(),
            User(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword').save(),
            User(username='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword').save(),
            User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword').save(),
        ]

        # Create teams
        team1 = Team(name='Blue Team', members=[users[0], users[1]]).save()
        team2 = Team(name='Gold Team', members=[users[2], users[3], users[4]]).save()

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=int(timedelta(hours=1).total_seconds())).save(),
            Activity(user=users[1], activity_type='Crossfit', duration=int(timedelta(hours=2).total_seconds())).save(),
            Activity(user=users[2], activity_type='Running', duration=int(timedelta(hours=1, minutes=30).total_seconds())).save(),
            Activity(user=users[3], activity_type='Strength', duration=int(timedelta(minutes=30).total_seconds())).save(),
            Activity(user=users[4], activity_type='Swimming', duration=int(timedelta(hours=1, minutes=15).total_seconds())).save(),
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100).save(),
            Leaderboard(user=users[1], score=90).save(),
            Leaderboard(user=users[2], score=95).save(),
            Leaderboard(user=users[3], score=85).save(),
            Leaderboard(user=users[4], score=80).save(),
        ]

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event').save(),
            Workout(name='Crossfit', description='Training for a crossfit competition').save(),
            Workout(name='Running Training', description='Training for a marathon').save(),
            Workout(name='Strength Training', description='Training for strength').save(),
            Workout(name='Swimming Training', description='Training for a swimming competition').save(),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
