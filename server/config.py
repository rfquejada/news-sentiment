import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool
from dotenv import load_dotenv
from newsdataapi import NewsDataApiClient


load_dotenv()

# Load environment variables from .env file
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = os.getenv("NEWS_API_URL")

# Initialize the NewsDataApiClient with the API key
newsapi = NewsDataApiClient(NEWS_API_KEY)

# Define the configuration for the database connection
DB_STRING = os.getenv("DB_STRING")

engine = create_engine(DB_STRING, client_encoding='utf8', poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=300)
try:
   connection = engine.connect()
   print("Successfully connected to the database!")
   connection.close()
except Exception as e:
   print(f"Error connecting to database: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()