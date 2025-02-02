# config.py

import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")  # Use environment variable
    DATABASE_NAME = os.getenv("DATABASE_NAME", "corider_db")          # Database name
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "users")           # Collection name