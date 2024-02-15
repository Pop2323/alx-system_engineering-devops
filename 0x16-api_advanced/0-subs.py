#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and prints
        the titles of the first 10 hot posts
        listed for a given subreddit."""
    headers = {'User-Agent': 'Custom'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
