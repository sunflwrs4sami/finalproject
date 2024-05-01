import requests

def get_skincare_makeup_tips():
    # Your function implementation here

    url = "https://world.openbeautyfacts.org/api/v2/tips"
    params = {
        "json": 1,
        "count": 5  # Example: Limit to 5 tips for skincare/makeup
        # Add any other parameters as needed
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        tips = [tip['text'] for tip in data['tips']]
        return tips
    else:
        return ["Moisturize your skin daily.", "Use sunscreen to protect your skin from UV rays.", "Blend your makeup well for a natural look."]  # Default tips if API call fails
