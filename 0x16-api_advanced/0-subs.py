#!/usr/bin/python3
"""retreives the amount of subscribers from reddit"""
import requests

def number_of_subscribers(subreddit):
    """Takes in the subreddit to look for"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
                "User-Agent": "linux_LTS:0x16.api.advanced:v1.0.0"
            }
    api_subscribers_data = requests.get(url, headers=headers, allow_redirects=False)
    if api_subscribers_data.status_code == 200:
        api_subscribers = api_subscribers_data.json()
        number_of_subscribers = api_subscribers['data']['subscribers']
        return number_of_subscribers
    elif api_subscribers_data.status_code == 404:
        return 0
