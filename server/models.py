from pydantic import BaseModel
from typing import List, Optional

class Article(BaseModel):
    title: str
    link: str
    description: Optional[str] = None
    source_url: str
    pubDate: str
    category: str
    image_url: Optional[str] = None


class NewsResponse(BaseModel):
    articles: List[Article]
    total_articles: int = 0
