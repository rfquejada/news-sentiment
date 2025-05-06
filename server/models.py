from pydantic import BaseModel
from typing import List

class Article(BaseModel):
    title: str
    description: str
    content: str
    source: str
    published_at: str
    sentiment: str

class NewsResponse(BaseModel):
    articles: List[Article]
