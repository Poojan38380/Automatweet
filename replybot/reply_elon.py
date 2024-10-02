# #TODO: id=44196397 elonmusk userid

import feedparser
import random

def get_elon_tweets(rss_url="https://rss.app/feeds/dLi2xqzEQnqqwPyw.xml", limit=1): #can create a rss feed of your favourite celeb related to your niche.
    # Replace with your RSS feed URL
    feed = feedparser.parse(rss_url)

    tweets = []

    # Extracting tweet messages, IDs, and user who posted the tweet
    for i, entry in enumerate(feed.entries[:limit]):  # Limiting to the specified number of tweets
        tweet_id = entry.link.split('/')[-1]  # Extract tweet ID from URL
        tweet_message = entry.title  # Tweet message
        tweet_user = entry.author  # Extract the user who posted the tweet
        tweets.append({'tweet_id': tweet_id, 'message': tweet_message, 'user': tweet_user})
        
    return tweets


def get_single_elon_tweet():
    tweets = get_elon_tweets()
    return random.choice(tweets)  # Selects a random tweet


