def post_tweet(client, tweet):
    try:
        response = client.create_tweet(text=tweet)
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Error posting tweet: {e}")