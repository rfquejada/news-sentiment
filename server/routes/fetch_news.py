from fastapi import APIRouter, Depends
from requests import Session
from config import get_db
from services.fetch_news import fetch_news
from models import NewsResponse

router = APIRouter()

@router.get("/fetch-news", response_model=NewsResponse)
def get_news(
    db: Session = Depends(get_db),
    max_pages: int = 50,
    max_articles: int = 15,
):
    articles = fetch_news(db=db, max_pages=max_pages, max_articles=max_articles)
    return {
        "articles": articles, 
        "total_articles": len(articles)
        }
