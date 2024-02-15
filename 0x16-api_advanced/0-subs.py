#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns
        the number of subscribers"""
    headers = {'User-Agent': 'Custom'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (requests.json().get('data').get('subscribers'))
    return (0)
