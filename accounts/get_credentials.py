from accounts.mongo import twitter_accounts_collection
from utils.print_color_utils import print_error, print_success

def get_twitter_account_details(username):
    try:
        # Retrieve the account details from the collection based on the username
        account_details = twitter_accounts_collection.find_one({"username": username}, {"_id": 0})

        if account_details:
            print_success(f"Account details for '{username}' retrieved successfully.")
            return account_details
        else:
            print_error(f"No account found for the username '{username}'.")
            return None
    except Exception as e:
        print_error(f"Failed to retrieve account details: {e}")
        return None
