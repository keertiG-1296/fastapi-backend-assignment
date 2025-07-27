from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:keerti%406336@localhost:5432/kpa_db"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("✅ Database connected successfully!")
except Exception as e:
    print("❌ Database connection failed:", e)
