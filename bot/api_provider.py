import tweepy
from utils.print_color_utils import print_error, print_success

def get_twitter_api(account_data):
    try:
        # Extract credentials from the provided account data
        username = account_data.get('username')
        api_key = account_data.get('api_key')
        api_secret = account_data.get('api_secret')
        access_token = account_data.get('access_token')
        access_token_secret = account_data.get('access_token_secret')

        # Check if all required fields are available
        if not all([ api_key, api_secret, access_token, access_token_secret]):
            print_error(f" ${username} -- Missing one or more API credentials. Please check the account data.")
            return None

        # Authenticate to Twitter API v2
        auth  = tweepy.OAuth1UserHandler(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        api = tweepy.API(auth)
        print_success(f"${username} -- Successfully authenticated Twitter API.")
        return api

    except Exception as e:
        print_error(f"${username} -- Failed to authenticate Twitter client: {e}")
        return None

