#!/usr/bin/python
import requests

def number_of_subscribers(subreddit):
    """Takes in the subreddit to look for"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
                "User-Agent": "linux_LTS:0x16.api.advanced:v1.0.0"
            }
    try:
        api_subscribers_data = requests.get(url, headers=headers, allow_redirects=False)
        if api_subscribers_data.status_code == 200:
            api_subscribers = api_subscribers_data.json()
            number_of_subscribers = api_subscribers['data']['subscribers']
            return number_of_subscribers
        else:
            return 0
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
