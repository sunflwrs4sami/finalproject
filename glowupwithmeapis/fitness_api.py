import requests
def get_workout_plan():
    url = "https://wger.de/api/v2/exercise/"
    params = {
        "format": "json",
        "limit": 5,  # Example: Limit to 5 exercises for the workout plan
        # Add any other parameters as needed
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        workout_plan = [exercise['name'] for exercise in data['results']]
        return workout_plan
    else:
        return ["Push-ups", "Squats", "Plank", "Jumping Jacks"]  # Default workout plan if API call fails
