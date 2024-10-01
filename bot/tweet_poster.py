from utils.print_color_utils import print_header,print_error,print_success,print_warning,print_info,print_highlight,print_debug,get_user_input

def post_tweet(client, tweet):
    try:
        response = client.create_tweet(text=tweet)
        print_success(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
    except Exception as e:
        print_error(f"Error posting tweet: {e}")