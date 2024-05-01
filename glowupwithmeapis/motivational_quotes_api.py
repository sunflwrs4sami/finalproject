import requests

def get_motivational_quotes():
    url = "https://quotes.rest/qod?category=inspire"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data['contents']['quotes'][0]['quote']
        return [quote]
    else:
        return ["The only way to do great work is to love what you do. – Steve Jobs", "Believe you can and you're halfway there. – Theodore Roosevelt", "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill"]  # Default quotes if API call fails
