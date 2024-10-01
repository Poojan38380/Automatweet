from utils.print_color_utils import print_header, print_error, print_success, print_warning, print_info, get_user_input
from accounts.select_accounts import select_twitter_account
from accounts.mongo import twitter_accounts_collection

def get_topics_by_username(username):
    try:
        account = twitter_accounts_collection.find_one({"username": username}, {"_id": 0, "topics": 1})
        return account.get("topics", []) if account else []
    except Exception as e:
        print_error(f"Failed to retrieve topics for the account: {e}")
        return []

def update_account_topics(username, topics):
    try:
        result = twitter_accounts_collection.update_one({"username": username}, {"$set": {"topics": topics}})
        return result.modified_count > 0
    except Exception as e:
        print_error(f"Failed to update topics for the account: {e}")
        return False

def add_topics_to_twitter_account():
    username = select_twitter_account("Select a Twitter account to add topics")

    if not username:
        print_error("No valid account selected.")
        return

    current_topics = get_topics_by_username(username)
    print_info(f"Current topics for account '{username}': {', '.join(current_topics) if current_topics else 'None'}")

    new_topics = [topic.strip() for topic in get_user_input("Enter new topics to add (separated by commas): ").split(",") if topic.strip()]

    if not new_topics:
        print_error("No topics were entered.")
        return

    combined_topics = list(set(current_topics + new_topics))

    if update_account_topics(username, combined_topics):
        print_success(f"Topics successfully updated for account '{username}'.")
    else:
        print_warning(f"No changes made to account '{username}'.")

def remove_topics_from_twitter_account():
    username = select_twitter_account("Select a Twitter account to remove topics")

    if not username:
        print_error("No valid account selected.")
        return

    current_topics = get_topics_by_username(username)

    if not current_topics:
        print_info(f"No topics found for account '{username}'.")
        return

    print_info(f"Current topics for account '{username}':")
    for i, topic in enumerate(current_topics, start=1):
        print_info(f"{i}. {topic}")

    try:
        indexes_to_remove = [int(i.strip()) - 1 for i in get_user_input("Enter the numbers of topics to remove (separated by commas): ").split(",") if i.strip()]

        if any(i < 0 or i >= len(current_topics) for i in indexes_to_remove):
            print_error("Invalid topic numbers entered.")
            return

        remaining_topics = [topic for i, topic in enumerate(current_topics) if i not in indexes_to_remove]

        if update_account_topics(username, remaining_topics):
            print_success(f"Topics successfully updated for account '{username}'.")
        else:
            print_warning(f"No changes made to account '{username}'.")

    except ValueError:
        print_error("Invalid input. Please enter valid numbers separated by commas.")



def get_topics_for_all_accounts():
    try:
        accounts = twitter_accounts_collection.find({}, {"_id": 0, "username": 1, "topics": 1})
        all_accounts_topics = {account['username']: account.get('topics', []) for account in accounts}
        return all_accounts_topics
    except Exception as e:
        print_error(f"Failed to retrieve topics for all accounts: {e}")
        return {}