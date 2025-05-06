import uuid
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, DateTime, Float, String, func, UUID
from config import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    article_id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    link = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    source_url = Column(String, nullable=False)
    pubDate = Column(DateTime(timezone=True), server_default=func.now())
    category = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    sentiment = Column(String, nullable=True)
    sentiment_score = Column(Float, nullable=True)

class ArticleOut(BaseModel):
    title: str
    link: str
    description: Optional[str] = None
    source_url: str
    pubDate: str
    category: str
    image_url: Optional[str] = None
    sentiment: Optional[str] = None
    sentiment_score: Optional[float] = None


class NewsResponse(BaseModel):
    articles: List[ArticleOut]
    total_articles: int = 0
