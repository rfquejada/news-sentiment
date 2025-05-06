from fastapi import APIRouter
from services.fetch_news import fetch_news
from models import NewsResponse

router = APIRouter()

@router.get("/fetch-news")
def get_news():
    articles = fetch_news()
    return {"articles": articles}
