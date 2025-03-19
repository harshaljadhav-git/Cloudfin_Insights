# Cloudfin_Insights
# AWS Data Pipeline: Lambda(Bank APIs) → S3 → Glue → RDS  → S3 → Glue → QuickSight

## 🚀 Overview
This project demonstrates an end-to-end **AWS Data Pipeline** for financial transaction data.  
It automates data extraction, transformation, and visualization using **AWS Lambda, Glue, EventBridge, and QuickSight**.

## 🏗️ Architecture
1️⃣ **Lambda Function**: Extracts data from **RDS (MySQL)** and uploads it to **S3**.  
2️⃣ **AWS Glue Job**: Transforms and loads the cleaned data back into **RDS**.  
3️⃣ **EventBridge Rule**: Automates data extraction every hour.  
4️⃣ **Amazon QuickSight**: Creates a **dashboard visualization** of transaction data.  

![Architecture Diagram](docs/pipeline-architecture.png)

## 🔧 Technologies Used
- **AWS Lambda** (ETL: RDS → S3)
- **AWS Glue** (Transform & Load)
- **Amazon S3** (Storage)
- **AWS RDS (MySQL)** (Database)
- **Amazon EventBridge** (Automation)
- **Amazon QuickSight** (Visualization)

## 📌 Setup Instructions
1️⃣ **Deploy Lambda Function:** Upload `rds_to_s3.py` in AWS Lambda.  
2️⃣ **Create Glue Job:** Run `s3_to_rds.py` as a Glue job.  
3️⃣ **Set Up EventBridge Rule:** Use `lambda_trigger.json` to trigger Lambda every hour.  
4️⃣ **Create QuickSight Dashboard:** Import `dashboard_config.json` into QuickSight.  

## 📊 Dashboard Preview
![QuickSight Dashboard](docs/dashboard-screenshot.png)

---
🔗 **Follow me on [GitHub](https://github.com/harshaljadhav-git) for more AWS projects!** 🚀
