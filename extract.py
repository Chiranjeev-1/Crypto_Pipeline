import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract():
    logging.info("Starting extraction from CoinGecko...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        logging.info(f"Extracted {len(response.json())} records")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Extraction failed: {e}")
        raise