#!/usr/bin/python3
"""recursievly retrieves data from subreddit"""
import requests


def recurse(subreddit, hot_list=None, after="", i=0):
    """Function that calls recursively"""

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {
                "User-Agent": "linux_LTS:0x16.api.advanced:v1.0.0"
            }
    api_title_data = requests.get(url, headers=headers, allow_redirects=False)
    if api_title_data.status_code == 200:
        api_title = api_title_data.json()
        new_after = api_title['data']['after']
        children = api_title['data']['children']
        for child in children:
            title = ""
            title = child['data']['title']
            hot_list.append(title)
            i = i + 1
        if new_after is None or i >= 100:
            return hot_list.sort()
        else:
            return recurse(subreddit, new_after, i)
