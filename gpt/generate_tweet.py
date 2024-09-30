import random
from g4f.client import Client
from bot.hashtags import get_saved_hashtags

def generate_tweet():
    client = Client()

    # Fetch the list of trending hashtags
    hashtags = get_saved_hashtags()

    # Define a list of topics
    topics = [
        "web development",
        "NextJs",
        "automation in everyday tasks",
        "social media marketing",
        "entrepreneurship",
        "AI transforming industries",
        "startup founder",
        "ReactJs",
        "AI",
        "startup life",
        "Elon Musk",
        "Free will",
    ]

    # Randomly choose a topic and a hashtag
    topic = random.choice(topics)
    hashtag = random.choice(hashtags)

    # Create the prompt with the chosen topic and hashtag
    prompt = (
        f"Write a short, sarcastic, creative, and unique tweet about {topic} "
        f"and include the hashtag {hashtag}. Make it engaging and relevant to tech enthusiasts. "
        f"(No need to add extra hashtags)"
        f"(Keep it under 280 characters)"
    )

    # Generate tweet content using GPT-3.5
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
