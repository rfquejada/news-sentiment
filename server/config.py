from dotenv import load_dotenv
import os
from newsdataapi import NewsDataApiClient

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = os.getenv("NEWS_API_URL")

newsapi = NewsDataApiClient(NEWS_API_KEY)