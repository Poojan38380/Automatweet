import requests
import os

from accounts.mongo import hashtags_collection
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()
def get_ritelit_hashtags():
    headers = {
        'Authorization': f"Bearer {os.getenv('RITEKIT_BEARER_TOKEN')}"
    }

    # Request the trending hashtags from the RiteKit API
    response = requests.get('https://api.ritekit.com/v1/search/trending?green=1&latin=1', headers=headers)

    # Parse the response as JSON
    trending_data = response.json()

    # Extract the hashtags and store them in a list
    hashtags = [f"#{hashtag['tag']}" for hashtag in trending_data['tags']]

    # Update the single document with the new hashtags list
    hashtags_collection.update_one(
        {},  # Find the document (if no filter, it will update the first found)
        {'$set': {'hashtags': hashtags}},  # Overwrite the hashtags list
        upsert=True  # If the document doesn't exist, insert it
    )

    # Optionally, print out the hashtags
    for hashtag in hashtags:
        print(hashtag)

def get_saved_hashtags():
    # Retrieve the document containing the hashtags
    document = hashtags_collection.find_one({}, {'_id': 0, 'hashtags': 1})  # Exclude _id from the result
    
    # Return the list of hashtags, or an empty list if not found
    return document['hashtags'] if document else []


