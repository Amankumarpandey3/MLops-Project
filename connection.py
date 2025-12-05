from pymongo import MongoClient
import pandas as pd

CONNECTION_URL = "mongodb+srv://amankumarpandey1712004_db_user:kumar12345@cluster0.8wgvo60.mongodb.net/"
DB_NAME = "Proj1"
COLLECTION_NAME = "Iris-Data"

client = MongoClient(CONNECTION_URL)
database = client[DB_NAME]
collection = database[COLLECTION_NAME]

# Fetch data
data = list(collection.find())
print(f"Number of documents fetched: {len(data)}")
print(data)

# Convert to dataframe
df = pd.DataFrame(data)
print(f"Dataframe shape: {df.shape}")
print(df.head())