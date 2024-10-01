import sys
from poster import post_to_single_account,post_5_strategy
from utils.print_color_utils import print_header,print_error,print_success,print_warning,print_info,print_highlight,print_debug,get_user_input

def wait_for_enter():
    input("Press Enter to continue...")

def main():
    """Main function to manage posting tweets to various accounts."""
    actions = {
        1: post_to_single_account,
        2: post_5_strategy,  
        3: sys.exit,
    }

    while True:
        print_header("Post Reels")
        print("1. Post to a single account")
        print("2. Post to single account")
        print("3. Exit")

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
