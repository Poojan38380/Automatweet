from utils.print_color_utils import print_info
from gpt.generate_prompt import create_tweet_prompt
from gpt.gpt_client import use_gpt
prompt= create_tweet_prompt()
print_info(f"Generated prompt: {prompt}")
tweet = use_gpt(prompt)
print(tweet)