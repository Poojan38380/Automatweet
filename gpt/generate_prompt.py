import random
from utils.print_color_utils import print_header, print_error, print_success, print_warning, print_info, get_user_input

wildcards = [
    "mention a famous twitter user",
    "use a bunch of emojis",
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
    # 50% chance to use a keyword or wildcard
    use_keyword = random.choice([True, False])

    # Select random wildcard or keyword
    if use_keyword and keywords:
        keyword = random.choice(keywords)

    
        # Randomly decide whether to add tag/hashtag
        use_hashtag = random.choice([True, False])
        
        # Randomly decide whether to add a celebrity mention
        use_tag_celebrity = random.choice([True, False])
        
        # Create a base prompt for the LLM to generate a sarcastic tweet
        prompt = f"""Tweet something sarcastic about {keyword} that could go viral.
        - Keep it within the 280 character limit.
        - Avoid using emojis.
        - The tweet should have a witty, humorous, and sharp tone that resonates with the audience. """

        # Add hashtags instruction if selected
        if use_hashtag:
                prompt += f"\nFeel free to include trending hashtags based on current global events or trends related to {keyword}."

        # Add mention instruction if selected
        if use_tag_celebrity:
                prompt += f"\nFeel free to tag any relevant famous person who could add to the viral potential."

    else:
        topic = random.choice(wildcards)

        prompt = f""""{topic}".
- Tweet something sarcastic or funny.
- Keep it within the 280 character limit.
- Avoid using emojis."""
        
        # Randomly decide whether to add a celebrity mention
        use_tag_celebrity = random.choice([True, False])
        
        # Add mention instruction if selected
        if use_tag_celebrity:
                prompt += f"\nFeel free to tag any relevant famous person."
        

    return prompt
