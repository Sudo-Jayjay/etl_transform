from extract.extract_users import extract_users
from transform.clean_users import clean_users
from transform.enrich_users import enrich_users
from load.save_users import save_to_csv

RAW_PATH = "data/raw/users.json"
STAGING_PATH = "data/staging/users_cleaned.csv"
PROCESSED_PATH = "data/processed/users_final.csv"

def run_pipeline():
    # Extract
    raw_data = extract_users(RAW_PATH)

    # Transform (staging)
    cleaned_data = clean_users(raw_data)
    save_to_csv(cleaned_data, STAGING_PATH)

    # Transform (final)
    enriched_data = enrich_users(cleaned_data)
    save_to_csv(enriched_data, PROCESSED_PATH)

if __name__ == "__main__":
    run_pipeline()