import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

def load(df):
    logging.info("Starting load to PostgreSQL...")
    
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        raise ValueError("DATABASE_URL not found in environment variables")
    
    engine = create_engine(database_url)
    
    # Create table if it doesn't exist
    create_table_sql = text("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id VARCHAR(100),
            symbol VARCHAR(20),
            name VARCHAR(100),
            current_price FLOAT,
            market_cap BIGINT,
            total_volume BIGINT,
            price_change_percentage_24h FLOAT,
            circulating_supply FLOAT,
            extracted_at TIMESTAMP
        )
    """)
    
    with engine.connect() as conn:
        conn.execute(create_table_sql)
        conn.commit()
    
    # Load data
    df.to_sql("crypto_prices", engine, if_exists="append", index=False)
    
    logging.info(f"Loaded {len(df)} records into crypto_prices table")