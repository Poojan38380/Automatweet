from accounts.mongo import twitter_accounts_collection
from utils.print_color_utils import print_header,print_error,print_success,print_warning,print_info,print_highlight,print_debug,get_user_input
from bot.client_provider import verify_twitter_credentials

def add_twitter_account():
    print_header("Add a new Twitter account")

    username = get_user_input("Enter Twitter username: ")
    api_key = get_user_input("Enter API_KEY: ")
    api_secret = get_user_input("Enter API_SECRET: ")
    bearer_token = get_user_input("Enter BEARER_TOKEN: ")
    access_token = get_user_input("Enter ACCESS_TOKEN: ")
    access_token_secret = get_user_input("Enter ACCESS_TOKEN_SECRET: ")

    if not username or not api_key or not api_secret or not bearer_token or not access_token or not access_token_secret:
        print_error("All fields are required.")
        return

    try:
        # Check if the account already exists
        if twitter_accounts_collection.find_one({"username": username}):
            print_error(f"Username '{username}' already exists. Please choose a different one.")
            return
    except Exception as e:
        print_error(f"Failed to check for existing username: {e}")
        return
    
        # Check if the credentials are valid before saving
    if not verify_twitter_credentials(api_key, api_secret, bearer_token, access_token, access_token_secret):
        print_error("Invalid Twitter API credentials. Please check and try again.")
        return

    try:
        # Insert the new Twitter account details
        twitter_accounts_collection.insert_one({
            "username": username,
            "api_key": api_key,
            "api_secret": api_secret,
            "bearer_token": bearer_token,
            "access_token": access_token,
            "access_token_secret": access_token_secret
        })
        print_success(f"Twitter account for '{username}' added successfully.")
    except Exception as e:
        print_error(f"Failed to add Twitter account: {e}")
