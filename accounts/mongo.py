from pymongo import MongoClient
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# MongoDB Atlas connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.automatweet
twitter_accounts_collection = db.twitter_accounts
