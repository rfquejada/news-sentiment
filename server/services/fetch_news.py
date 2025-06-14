import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from config import NEWS_API_URL, NEWS_API_KEY
from models import Article
from services.sentiment_analyzer import analyze_sentiment


def fetch_news(db, max_pages=50, max_articles=15):
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

    for article in collected_articles:
        sentiment, score = analyze_sentiment(
            title=article["title"],
            description=article["description"] if article["description"] else "",
            categories=article["category"]
        )

        article["sentiment"] = sentiment
        article["sentiment_score"] = score

    # Replace the existing articles in the database with the new ones
    db.query(Article).delete()
    db.commit()
    for article in collected_articles:
        db_article = Article(
            article_id=article["article_id"],
            title=article["title"],
            link=article["link"],
            description=article["description"],
            source_url=article["source_url"],
            pubDate=article["pubDate"],
            category=article["category"],
            image_url=article["image_url"],
            sentiment=article["sentiment"],
            sentiment_score=article["sentiment_score"]
        )
        db.add(db_article)
    db.commit()
    db.refresh(db_article)

    db.close()

    return collected_articles