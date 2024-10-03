def generate_gpt_prompt(tweet):
    # Extract the person mentioned and the tweet content
    try:
        mention, tweet_content = tweet.split(":", 1)
        mention = mention.strip()
        tweet_content = tweet_content.strip()
    except ValueError:
        return "Invalid tweet format. Please follow the format: '@username: tweet message'"

    # Construct the prompt for GPT
    prompt = (f"""A tweet from {mention} and it says: '{tweet_content}'. "
Keeping in mind the current global scenario, create a, viral-worthy short reply tweet. "
Keep the tone smart.(avoid emojis and keep under 280 characters)(just give the tweet)""")

    return prompt