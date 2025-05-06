from fastapi import APIRouter
from services.fetch_news import fetch_news
from models import NewsResponse

router = APIRouter()

@router.get("/fetch-news", response_model=NewsResponse)
def get_news():
    articles = fetch_news()
    return {
        "articles": articles, 
        "total_articles": len(articles)
        }
