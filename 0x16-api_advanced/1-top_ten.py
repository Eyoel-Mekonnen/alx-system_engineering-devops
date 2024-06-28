#!/usr/bin/python3
""" Retrieve the 10 hot posts title"""
import requests


def top_ten(subreddit):
    """function that retreives titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
                "User-Agent": "linux_LTS:0x16.api.advanced:v1.0.0"
            }
    api_title_data = requests.get(url, headers=headers, allow_redirects=False)
    api_title = api_title_data.json()
    if api_title_data.status_code == 200:
        for i in range(0, 10):
            title = api_title['data']['children'][i]['data']['title']
            print(title)
    else:
        print("None")
