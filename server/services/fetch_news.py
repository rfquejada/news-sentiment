import requests
from config import NEWS_API_URL, NEWS_API_KEY


def fetch_news(max_pages=50, max_articles=15):
    base_url = f"{NEWS_API_URL}/latest"
    headers = {
        "accept": "application/json",
        "Authorization": NEWS_API_KEY,
        "Content-Type": "application/json"
    }

    params = {
        "apikey": NEWS_API_KEY,
        "country": "ph"
    }

    trusted_sources = [
        "inquirer",
        "gmanetwork", "gma news", "gma",
        "abs-cbn", "abscbn", "abs cbn",
        "tv5", "news5", "interaksyon",
        "philstar", "philippine star",
        "mb.com.ph", "manila bulletin"
    ]

    collected_articles = []
    page_count = 0
    next_page = None

    while page_count < max_pages and len(collected_articles) < max_articles:
        if next_page:
            params["page"] = next_page
        else:
            params.pop("page", None)

        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error fetching news: {response.status_code}")
            break

        data = response.json()
        articles = data.get('results', [])
        next_page = data.get('nextPage', None)

        for article in articles:
            if len(collected_articles) >= max_articles:
                break

            source = article.get('source_url', '') or ''
            creator = str(article.get('creator', ''))

            combined = f"{source} {creator}".lower()
            if any(keyword in combined for keyword in trusted_sources):
                cleaned_article = {
                    "article_id": article.get('article_id'),
                    "title": article.get('title'),
                    "link": article.get('link'),
                    "description": article.get('description'),
                    "source_url": article.get('source_url'),
                    "pubDate": article.get('pubDate'),
                    "category": ", ".join(article.get('category', [])) if isinstance(article.get('category'), list) else article.get('category', ''),
                    "image_url": article.get('image_url'),
                }
                collected_articles.append(cleaned_article)

        page_count += 1

        if not next_page:
            print("No more pages available.")
            break

    print(f"{len(collected_articles)} trusted articles fetched")
    return collected_articles