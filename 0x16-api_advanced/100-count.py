#!/usr/bin/python3
"""Recurssivley retives title from reddis api"""
import re
import requests


def count_words(subreddit, word_list, after="", dict_words=None, i=0):

    if dict_words is None:
        dict_words = {}
        for word in word_list:
            if re.match(r'^[a-zA-Z]+$', word):
                word = word.lower()
                dict_words[word] = 0
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {
                "User-Agent": "linux_LTS:0x16.api.advanced:v1.0.0"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        api_title = response.json()
        children = api_title['data']['children']
        after = api_title['data']['after']
        for child in children:
            child_word = child['data']['title'].split()
            child_word = [ch.lower() for ch in child_word]
            for key, value in dict_words.items():
                if key in child_word:
                    dict_words[key] = value + 1
    if after and i < 100:
        i = i+1
        return count_words(subreddit, word_list, after,  dict_words, i)
    else:
        for key, value in sorted(dict_words.items()):
            if value != 0:
                print("{}: {}".format(key, value))
