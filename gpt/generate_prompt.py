import random
from utils.print_color_utils import print_header, print_error, print_success, print_warning, print_info, get_user_input

wildcards = [
    "mention a famous twitter user",
    "ask people to follow your account",
    "try to inspire the audience",
    "talk shit about something random",
    "give a shoutout to anyone",
    "incorporate a trendy topic",
    "talk about the joy of being a sentient being",
    "threaten to give up on #twitter",
    "say hi to someone's mom",
    "push a cryptocurrency or memecoin",
    "brag about your achievements",
    "write an unhinged manifesto",
    "argue about politics",
    "promulgate a conspiracy theory",
    "talk about what you ate for dinner",
    "brag about how much you can bench press",
    "advocate for privacy",
    "say you just changed your twitter banner"
]

def create_tweet_prompt(keywords=[]):
    # 70% chance to use a keyword or 30% to use a wildcard
    use_keyword = random.random() < 0.7

    # Select random wildcard or keyword
    if use_keyword and keywords:
        keyword = random.choice(keywords)

        # Randomly decide whether to add tag/hashtag
        use_hashtag = random.choice([True, False])
        
        # Randomly decide whether to add a celebrity mention
        use_tag_celebrity = random.choice([True, False])
        
        # Create a base prompt for the LLM to generate a sarcastic tweet
        prompt = f"""Write a sarcastic tweet that is sharp and likely to go viral about "{keyword}".
- Maximum 280 characters.
- Avoid using emojis.
- Make it witty, edgy, and humorous, with a tone that grabs attention immediately.
- Make the audience feel part of an inside joke, encouraging retweets and comments."""

        # Add hashtags instruction if selected
        if use_hashtag:
            prompt += f"\n- Add a trending hashtag related to {keyword} or current global events for extra traction."

        # Add mention instruction if selected
        if use_tag_celebrity:
            prompt += f"\n- Consider tagging a famous person or influencer for extra virality."

    else:
        topic = random.choice(wildcards)

        prompt = f""""{topic}".
- Write a sarcastic or humorous tweet.
- Keep it under 280 characters.
- Avoid using emojis.
- Make the tone irreverent, witty, and instantly shareable.
- Use humor or irony to draw people in."""

        # Randomly decide whether to add a celebrity mention
        use_tag_celebrity = random.choice([True, False])
        
        # Add mention instruction if selected
        if use_tag_celebrity:
            prompt += f"\n- Optionally, tag a celebrity or influencer to boost engagement."
        
    return prompt
