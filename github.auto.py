import schedule
import time
from datetime import datetime
from accounts.select_accounts import select_twitter_account
from accounts.get_credentials import get_twitter_account_details, get_all_twitter_account_details
from accounts.topics import get_topics_by_username
from bot.auth_provider import get_twitter_client
from bot.tweet_poster import post_tweet
from gpt.generate_prompt import create_tweet_prompt
from gpt.gpt_client import use_gpt
from utils.print_color_utils import print_header, print_error, print_success, print_warning, print_info, print_highlight, print_debug, get_user_input

def single_account_poster_helper(username):
    try:
        credentials = get_twitter_account_details(username=username)
        topics = get_topics_by_username(username=username)
        prompt = create_tweet_prompt(keywords=topics)
        tweet = use_gpt(prompt=prompt)
        print(tweet)

        client = get_twitter_client(account_data=credentials)
        post_tweet(client=client, tweet=tweet)
        print_success(f"Successfully posted tweet for {username} at {datetime.now().strftime('%H:%M')}")
    except Exception as e:
        print_error(f"Failed to post tweet: {str(e)}")



if __name__ == "__main__":
    single_account_poster_helper("poojan_goyani")
