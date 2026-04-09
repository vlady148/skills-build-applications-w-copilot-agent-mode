from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Crear workouts
        w1 = Workout.objects.create(name='Cardio Blast', description='Intenso cardio de 30 minutos', difficulty='Medium')
        w2 = Workout.objects.create(name='Fuerza Total', description='Rutina de fuerza para todo el cuerpo', difficulty='Hard')

        # Crear actividades
        Activity.objects.create(user=tony, type='Running', duration=30, date=date.today())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=date.today())
        Activity.objects.create(user=clark, type='Yoga', duration=40, date=date.today())

        # Crear leaderboard
        Leaderboard.objects.create(user=tony, points=120)
        Leaderboard.objects.create(user=steve, points=110)
        Leaderboard.objects.create(user=bruce, points=130)
        Leaderboard.objects.create(user=clark, points=125)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
