import json

def extract_top_tweets(file_path="tweets.json", count=1):
    # Load the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Extract tweets data
    tweets = data['data']
    
    # Initialize an empty list to store the result
    extracted_tweets = []

    # Loop through the top 'count' tweets
    for tweet in tweets[:count]:
        tweet_info = {
            "full_text": tweet.get('full_text', ''),
            "user_id_str": tweet.get('user_id_str', ''),
            "id_str": tweet.get('id_str', '')
        }
        extracted_tweets.append(tweet_info)
    
    return extracted_tweets


