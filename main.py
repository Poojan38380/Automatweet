from accounts.select_accounts import select_twitter_account
from accounts.get_credentials import get_twitter_account_details
from accounts.addaccount import add_twitter_account
from bot.client_provider import get_twitter_client
from bot.tweet_poster import post_tweet

username = select_twitter_account("Select an account")

print(username)


details = get_twitter_account_details(username)

print(details)


client = get_twitter_client(details)

print(client)

post_tweet(client,"This is a tweet")