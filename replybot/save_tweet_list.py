from dotenv import load_dotenv
import os
import requests
import json

# Load environment variables from .env file
load_dotenv()

# MongoDB Atlas connection
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def save_tweets_from_list():
    url = "https://twitter-x-api.p.rapidapi.com/api/list/tweets"
    querystring = {"list_id": "1841357094005686535", "count": "10"}

    headers = {
        "x-rapidapi-key": f"{RAPIDAPI_KEY}",
        "x-rapidapi-host": "twitter-x-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Check if the response status code is 200 (OK) before processing
    if response.status_code == 200:
        tweet_data = response.json()

        # Save the data to a JSON file
        with open("tweets.json", "w") as json_file:
            json.dump(tweet_data, json_file, indent=4)

        print("Data saved to tweets.json")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
