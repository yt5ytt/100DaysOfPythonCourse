import os
import requests

POST_WORKOUT_ENDPOINT = os.environ.get("POST_WORKOUT_ENDPOINT")


class PostWorkout:

    def __init__(self, date, time, exercise, duration, calories):
        self.parameters = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
            }

        }

        self.response = requests.post(url=POST_WORKOUT_ENDPOINT, json=self.parameters)
        print(self.response.text)
