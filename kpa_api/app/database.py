from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:keerti%406336@localhost:5432/kpa_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


origins = [
    "http://localhost:3000",  # React or other frontend
    "http://127.0.0.1:3000",
    "*",  # Allow all (use only for testing, not in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],        # Allow all HTTP methods
    allow_headers=["*"],        # Allow all headers
)


@app.get("/")
def read_root():
    return {"message": "CORS is enabled!"}
