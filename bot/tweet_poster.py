def post_tweet(api, message):
    try:
        api.update_status(message)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {e}")
