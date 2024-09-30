from accounts.mongo import twitter_accounts_collection
from utils.print_color_utils import print_header,print_error,print_success,print_warning,print_info,print_highlight,print_debug,get_user_input

def select_twitter_account(action_message):
    try:
        # Retrieve all Twitter accounts from the collection
        accounts = list(twitter_accounts_collection.find({}, {"username": 1}))
    except Exception as e:
        print_error(f"Failed to retrieve Twitter accounts: {e}")
        return None

    if not accounts:
        print_error("No Twitter accounts found in the database.")
        return None

    print_header(action_message)
    # Display all Twitter account usernames with index numbers
    for index, account in enumerate(accounts, start=1):
        print(f"{index}. {account['username']}")

    try:
        # Get the user's selection
        choice = int(get_user_input("Enter the account number: "))
        if 1 <= choice <= len(accounts):
            # Return the selected username
            return accounts[choice - 1]["username"]
        else:
            print_error("Invalid selection. Please choose a valid number.")
    except ValueError:
        print_error("Please enter a valid number.")
    
    return None
