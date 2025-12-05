from pymongo import MongoClient
import pandas as pd

# MongoDB Connection Details
CONNECTION_URL = "mongodb+srv://amankumarpandey1712004_db_user:kumar12345@cluster0.8wgvo60.mongodb.net/"
DB_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"

try:
    # Establish Connection
    client = MongoClient(CONNECTION_URL)
    database = client[DB_NAME]
    collection = database[COLLECTION_NAME]

    # Test Connection
    print("MongoDB connection successful.")

    # Fetch Data
    data = list(collection.find())
    print(f"Number of documents fetched: {len(data)}")

    # Convert to DataFrame
    if data:
        df = pd.DataFrame(data)
        print(f"Dataframe shape: {df.shape}")
        print(df.head())
    else:
        print("No data found in the collection.")

except Exception as e:
    print(f"Error: {e}")