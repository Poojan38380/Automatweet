# #TODO: id=44196397 elonmusk userid

import feedparser
import random

def get_elon_tweets(rss_url="https://rss.app/feeds/JZFUSLjFbFnul62l.xml"): #can create a rss feed of your favourite celeb related to your niche.
    # Replace with your RSS feed URL
    feed = feedparser.parse(rss_url)

    tweets = []

    # Extracting tweet messages and IDs
    for i, entry in enumerate(feed.entries[:1]):  # Limiting to first 1 tweets
        tweet_id = entry.link.split('/')[-1]  # Extract tweet ID from URL
        tweet_message = entry.title  # Tweet message
        tweets.append({'tweet_id': tweet_id, 'message': tweet_message})

    return tweets


def get_single_elon_tweet():
    tweets = get_elon_tweets()
    return random.choice(tweets)  # Selects a random tweet


