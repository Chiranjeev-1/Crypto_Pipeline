import pandas as pd
import logging

def transform(raw_data):
    logging.info("Starting transformation...")
    
    df = pd.DataFrame(raw_data)
    
    # Keep only the columns we need
    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h",
        "circulating_supply"
    ]]
    
    # Drop any rows with missing values
    df.dropna(inplace=True)
    
    # Remove duplicates
    df.drop_duplicates(subset=["id"], inplace=True)
    
    # Clean up symbol — uppercase
    df["symbol"] = df["symbol"].str.upper().str.strip()
    
    # Add a timestamp so we know when this record was extracted
    df["extracted_at"] = pd.Timestamp.now()
    
    logging.info(f"Transformed {len(df)} records")
    return df