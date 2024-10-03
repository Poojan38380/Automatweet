import random
from utils.print_color_utils import print_header,print_error,print_success,print_warning,print_info,print_highlight,print_debug,get_user_input

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
    "say you just changed your twitter banner",
    "complain about slow Wi-Fi",
    "declare your love for coffee or tea",
    "confess your obsession with a random TV show",
    "rant about modern art",
    "say something controversial about pineapple on pizza",
    "talk about how you've quit social media 10 times",
    "give unsolicited life advice",
    "pretend you're a tech startup founder",
    "overhype a boring weekend plan",
    "mock astrology or horoscopes",
    "make fun of internet trends like TikTok dances",
    "talk about 'adulting' being hard",
    "talk about your 'genius' New Year's resolutions",
    "pretend you're running for president",
    "announce you're starting a podcast",
    "declare your love for a random historical figure",
    "give a shoutout to your 'haters'"
    "talk about how you woke up and chose violence",
    "brag about staying in bed all day",
    "declare war on Monday mornings",
    "pretend you're writing a bestseller novel",
    "mock people who use too many hashtags",
    "complain about influencer culture",
    "make fun of your morning routine",
    "talk about how you're 'totally fine' (you're not)",
    "discuss your complex relationship with carbs",
    "talk about binge-watching a new show",
    "give fake relationship advice",
    "pretend you're an expert on something you're not",
    "jokingly announce you're deleting the app",
    "brag about your non-existent workout routine",
    "joke about online dating disasters",
    "declare that you're moving to Mars",
    "rant about online shopping addictions",
    "complain about getting no retweets",
    "mock your obsession with collecting random facts",
    "talk about being 'deeply misunderstood'"    
]

def create_tweet_prompt(keywords=[]):
    # 70% chance to use a keyword or 30% to use a wildcard
    use_keyword = random.random() < 0.8

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
- Make the audience feel part of an inside joke, encouraging retweets and comments.
- Just return the tweet, nothing else."""

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
- Use humor or irony to draw people in.
- Just return the tweet, nothing else."""

        # Randomly decide whether to add a celebrity mention
        use_tag_celebrity = random.choice([True, False])
        
        # Add mention instruction if selected
        if use_tag_celebrity:
            prompt += f"\n- Optionally, tag a celebrity or influencer to boost engagement."
        
    return prompt
