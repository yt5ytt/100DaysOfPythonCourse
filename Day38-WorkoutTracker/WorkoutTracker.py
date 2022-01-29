from exercise import Exercise
from postWorkout import PostWorkout
import datetime
import time

today = datetime.date.today()
date = time.strftime("%d.%m.%Y.")
time = time.strftime("%H:%M:00")

query = input("What have your made of workouts today?\n")

exercise = Exercise(query=query)
exercises = exercise.data["exercises"]

for one in exercises:
    workout = one["name"].title()
    duration = one["duration_min"]
    calories = one["nf_calories"]
    post_workout = PostWorkout(date=date, time=time, exercise=workout, duration=duration, calories=calories)
