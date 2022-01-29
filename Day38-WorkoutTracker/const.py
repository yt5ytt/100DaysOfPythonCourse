import os

APP_ID = os.environ.get("NUTRITIONIX_ID")
API_KEY = os.environ.get("NUTRITIONIX_API")
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}
