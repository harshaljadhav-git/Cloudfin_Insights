import sys
import boto3
import json
from decimal import Decimal
from datetime import datetime
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType, TimestampType

# Initialize Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Read Data from S3
s3_bucket = "cloudfin-transaction-data"
s3_key = "processed_data/transactions.csv"
df = spark.read.csv(f"s3://{s3_bucket}/{s3_key}", header=True, inferSchema=True)

# Data Transformation
df = df.withColumn("amount", col("amount").cast(DecimalType(10,2))) \
       .withColumn("timestamp", col("timestamp").cast(TimestampType()))

# Write to RDS
df.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://database-1.cjigecus4bwc.ap-south-1.rds.amazonaws.com:3306/cloudfin_db") \
    .option("dbtable", "transactions_cleaned") \
    .option("user", "admin") \
    .option("password", "Harshal-2002-69") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .mode("append") \
    .save()

job.commit()
