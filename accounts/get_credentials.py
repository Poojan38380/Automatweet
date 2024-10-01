from accounts.mongo import twitter_accounts_collection
from utils.print_color_utils import print_header,print_error,print_success,print_warning,print_info,print_highlight,print_debug,get_user_input

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



def get_all_twitter_account_details():
    try:
        # Retrieve all account details from the collection, excluding the _id field
        all_accounts = twitter_accounts_collection.find({}, {"_id": 0})

        account_list = list(all_accounts)
        if account_list:
            print_success("All account details retrieved successfully.")
            return account_list
        else:
            print_error("No accounts found in the collection.")
            return []
    except Exception as e:
        print_error(f"Failed to retrieve account details: {e}")
        return []