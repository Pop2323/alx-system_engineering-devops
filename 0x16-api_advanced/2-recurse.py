#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API
"""
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """Write a recursive function that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        next_data = response.json().get('data').get('after')
        if next_data is not None:
            after = next_data
        hot_posts = response.json().get('data').get('children')
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))
        return (hot_list)
    else:
        return (None)
