from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.fetch_news import router as fetch_news_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "https://ics-star-app.vercel.app"
]

app.add_middleware(
    CORSMiddleware,

    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "Accept"],

)

app.include_router(fetch_news_router, prefix="/api", tags=["news"])