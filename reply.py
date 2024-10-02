from replybot.fetch_tweets_to_reply import get_elon_tweets,get_single_elon_tweet
from replybot.reply_prompt import generate_gpt_prompt
from gpt.gpt_client import use_gpt
from bot.tweet_poster import reply_to_tweet
from accounts.select_accounts import select_twitter_account
from accounts.get_credentials import get_twitter_account_details
from bot.auth_provider import get_twitter_client

def reply_main():

        username = select_twitter_account("Select account to post to:")
        credentials = get_twitter_account_details(username=username)
        client = get_twitter_client(account_data=credentials)
        
        elon_tweet=get_single_elon_tweet()
        message_content = elon_tweet["message"]
        tweet_id = elon_tweet["tweet_id"]
        posted_by = elon_tweet["user"]
        print(f"\n{posted_by} tweeted: {message_content}\n")
        prompt = generate_gpt_prompt(tweet=message_content)
        reply_tweet= use_gpt(prompt=prompt)
        print(f"Reply message : {reply_tweet}")

        reply_to_tweet(client=client, tweet=reply_tweet, tweet_id=tweet_id)

