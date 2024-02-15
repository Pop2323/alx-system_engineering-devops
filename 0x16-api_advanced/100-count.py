#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def count_words(subreddit, word_list):
    """Write a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted
    count of given keywords (case-insensitive, delimited by
    spaces. Javascript should count as javascript,
    but java should not).
"""
    word_counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()['data']
        posts = data['children']

        for post in posts:
            title = post['data']['title'].lower()

            for word in word_list:
                normalized_word = word.lower()
                count = title.count(normalized_word)
                word_counts[normalized_word] = word_counts.get(
                        normalized_word, 0) + count
        sorted_word_counts = sorted(
                word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            if count > 0:
                print(f'{word}: {count}')

    except requests.RequestException as e:
        print(f'Error fetching data from Reddit API: {e}')


count_words('programming', ['react', 'python', 'java',
            'javascript', 'scala', 'no_results_for_this_one'])
