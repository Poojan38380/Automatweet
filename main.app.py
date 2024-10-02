import sys
from manage import manage_accounts
from poster import post_to_single_account,post_5_strategy
from utils.print_color_utils import print_header,print_error,print_success,print_warning,print_info,print_highlight,print_debug,get_user_input
from reply import reply_main
from replybot.save_tweet_list import save_tweets_from_list

def main():
    """Main function to manage everything."""
    actions = {
        1: manage_accounts,
        2: post_to_single_account,  
        3: post_5_strategy,  
        4: reply_main,
        6: save_tweets_from_list,
        7: sys.exit,
    }

    while True:
        print_header("Post Reels")
        print("1. Manage Accounts")
        print("2. Post to single account")
        print("3. Post 5 times/day to a single account")
        print("4. Reply to the latest tweets in a curated list.")
        print("5. placeholder")
        print("5. Retrive the latest tweets from autoreply list")
        print("6. Exit")

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


if __name__ == "__main__":
    main()
