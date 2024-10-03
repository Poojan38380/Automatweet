from replybot.reply_prompt import generate_gpt_prompt
from gpt.gpt_client import use_gpt
from bot.tweet_poster import reply_to_tweet
from accounts.get_credentials import get_twitter_account_details
from bot.auth_provider import get_twitter_client
from replybot.fetch_tweets_to_reply import get_single_elon_tweet


def reply_to_user_tweet(username):
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

if __name__ == "__main__":
    reply_to_user_tweet("poojan_goyani")
