import logging
from extract import extract
from transform import transform
from load import load

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_pipeline():
    logging.info("Pipeline started...")
    
    try:
        raw_data = extract()
        df = transform(raw_data)
        load(df)
        logging.info("Pipeline completed successfully!")
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()