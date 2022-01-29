from const import HEADERS
import requests

EXERCISE_END = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = 100
HEIGHT = 188
AGE = 46


class Exercise:

    def __init__(self, query):
        parameters = {
            "query": query,
            "gender": GENDER,
            "weight_kg": WEIGHT,
            "height_cm": HEIGHT,
            "age": AGE,
        }
        self.response = requests.post(url=EXERCISE_END, headers=HEADERS, json=parameters)
        self.data = self.response.json()
