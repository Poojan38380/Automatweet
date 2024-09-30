import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')  # v2 requires a Bearer Token

# Authenticate to Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN, 
                       consumer_key=API_KEY, 
                       consumer_secret=API_SECRET, 
                       access_token=ACCESS_TOKEN, 
                       access_token_secret=ACCESS_TOKEN_SECRET)

def post_tweet():
    tweet = "Colleges have become status-stamping machines."
    try:
        response = client.create_tweet(text=tweet)
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

post_tweet()
