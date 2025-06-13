from time import strftime
from fastapi import APIRouter, Depends, HTTPException, Query
from requests import Session
from config import get_db
from models import Article, NewsOutList

router = APIRouter()

# Fetch all news articles from the database
@router.get("/fetch-news-articles", response_model = NewsOutList)
def get_news(
    db: Session = Depends(get_db),
    isPositive: bool = Query(None),
    isNegative: bool = Query(None),
    isNeutral: bool = Query(None),
):
    
    if isPositive:
        result = db.query(
            Article.title,
            Article.link,
            Article.description,
            Article.source_url,
            Article.pubDate,
            Article.image_url,
            Article.sentiment,
            Article.sentiment_score
        ).filter(Article.sentiment == "positive").all()

    elif isNegative:
        result = db.query(
            Article.title,
            Article.link,
            Article.description,
            Article.source_url,
            Article.pubDate,
            Article.image_url,
            Article.sentiment,
            Article.sentiment_score
        ).filter(Article.sentiment == "negative").all()

    elif isNeutral:
        result = db.query(
            Article.title,
            Article.link,
            Article.description,
            Article.source_url,
            Article.pubDate,
            Article.image_url,
            Article.sentiment,
            Article.sentiment_score
        ).filter(Article.sentiment == "neutral").all()

    else:
        result = db.query(
            Article.title,
            Article.link,
            Article.description,
            Article.source_url,
            Article.pubDate,
            Article.image_url,
            Article.sentiment,
            Article.sentiment_score
        ).all()
        
    if not result:
        raise HTTPException(status_code=404, detail="No articles found")
    
    articles = []
    for article in result:
        formatted_date = article.pubDate.strftime("%B %d, %Y %I:%M %p")
        articles.append({
            "title": article.title,
            "link": article.link,
            "description": article.description,
            "source_url": article.source_url,
            "pubDate": formatted_date,
            "image_url": article.image_url,
            "sentiment": article.sentiment,
            "sentiment_score": article.sentiment_score
        })

    return {
        "articles": articles,
        "total_articles": len(articles)
    }