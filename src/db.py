import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER", "bia_user")
    password = os.getenv("DB_PASS", "bia_pass")
    host = os.getenv("DB_HOST", "db")
    port = os.getenv("DB_PORT", "5432")
    db = os.getenv("DB_NAME", "bia_db")
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)

def init_db():
    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS enriched_postcodes (
            id SERIAL PRIMARY KEY,
            latitude FLOAT,
            longitude FLOAT,
            postcode TEXT,
            country TEXT,
            admin_area TEXT,                                        
            admin_district TEXT,
            region TEXT,
            quality INT,
            date_inserted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """))
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_postcode ON enriched_postcodes(postcode);") )