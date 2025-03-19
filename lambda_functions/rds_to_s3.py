import pymysql
import boto3
import csv
import os

# RDS Connection Details
rds_host = "database-1.cjigecus4bwc.ap-south-1.rds.amazonaws.com"
db_user = "admin"
db_password = "Harshal-2002-69"
db_name = "cloudfin_db"
table_name = "transactions"

# S3 Details
s3_bucket = "cloudfin-transaction-data"
s3_key = "processed_data/transactions.csv"

def lambda_handler(event, context):
    try:
        # Connect to RDS
        conn = pymysql.connect(host=rds_host, user=db_user, password=db_password, database=db_name)
        cursor = conn.cursor()
        
        # Fetch Data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        
        # Save to CSV
        csv_file = "/tmp/transactions.csv"
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(column_names)
            writer.writerows(rows)
        
        # Upload to S3
        s3_client = boto3.client("s3")
        s3_client.upload_file(csv_file, s3_bucket, s3_key)
        
        return {"status": "success", "message": f"Data uploaded to S3: s3://{s3_bucket}/{s3_key}"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
