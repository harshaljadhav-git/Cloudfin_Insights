import json
import boto3
import requests
import datetime
import os

# Bank API Details
BANK_API_URL = "https://api.yourbank.com/v1/transactions"
BANK_API_KEY = "your-api-key"

# AWS S3 Details
S3_BUCKET = "cloudfin-transaction-data"
S3_KEY_PREFIX = "raw_data/transactions_"

def fetch_bank_transactions():
    """Fetch transactions from bank API."""
    headers = {"Authorization": f"Bearer {BANK_API_KEY}"}
    params = {"from": "2024-03-01", "to": "2024-03-10"}  # Modify as needed

    response = requests.get(BANK_API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch transactions: {response.text}")

def upload_to_s3(data):
    """Upload transactions to S3."""
    s3_client = boto3.client("s3")
    file_name = f"{S3_KEY_PREFIX}{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    
    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=file_name,
        Body=json.dumps(data, indent=2),
        ContentType="application/json"
    )
    
    return f"s3://{S3_BUCKET}/{file_name}"

def lambda_handler(event, context):
    """AWS Lambda entry point."""
    try:
        transactions = fetch_bank_transactions()
        s3_path = upload_to_s3(transactions)
        
        return {
            "status": "success",
            "message": "Bank transactions fetched and stored successfully.",
            "s3_path": s3_path
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
