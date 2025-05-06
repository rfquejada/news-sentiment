import requests
from config import NEWS_API_URL, NEWS_API_KEY


def fetch_news():
    url = f"{NEWS_API_URL}/latest?apikey={NEWS_API_KEY}&country=ph"

    headers = {
        "accept": "application/json",
        "Authorization": NEWS_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    print(response.json())
    # else:
    #     print(f"Error fetching news: {response.status_code}")
    #     return []