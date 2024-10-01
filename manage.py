import sys
from accounts.topics import add_topics_to_twitter_account,remove_topics_from_twitter_account
from accounts.addaccount import add_twitter_account
from utils.print_color_utils import print_header,print_error,print_success,print_warning,print_info,print_highlight,print_debug,get_user_input


def manage_accounts():
    """Main function to manage posting tweets to various accounts."""
    actions = {
        1: add_twitter_account,
        2: add_topics_to_twitter_account,  
        3:remove_topics_from_twitter_account,
        4: sys.exit,
    }

    while True:
        print_header("Post Reels")
        print("1. Add a new account")
        print("2. Add topics to an account")
        print("3. Remove topics from an account")
        print("4. Exit")

        try:
            action = int(get_user_input("Choose an action: "))
            if action in actions:
                actions[action]()
            else:
                print_error("Invalid selection. Please choose a valid number.")
        except ValueError:
            print_error("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by user.\n")
            sys.exit(0)
        except Exception as e:
            print_error(f"Main process error: {str(e)}")