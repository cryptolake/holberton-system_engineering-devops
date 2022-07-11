#!/usr/bin/python3
"""Get hot posts from reddit sub."""


import requests


def count_words(subreddit, word_list, after='', hot_list={}):
    """Get posts of sub."""
    headers = {'User-Agent': "Mozilla/5.0"}
    url = 'https://www.reddit.com'
    res = requests.get(f'{url}/r/{subreddit}/hot.json?after={after}?limit=100',
                       headers=headers, allow_redirects=False)
    if res.status_code == 302:
        return None
    rj = res.json()
    if rj.get('data') is None:
        return None
    for post in rj['data']['children']:
        title = post['data']['title'].lower().split(' ')
        for word in title:
            if word in word_list and hot_list.get(word):
                if hot_list.get(word):
                    hot_list[word] += 1
                else:
                    hot_list[word] = 0

    if rj['data']['after'] is None:
        for word in sorted(hot_list, key=lambda x: x[1]):
            print(word[0], word[1])
            
    return count_words(subreddit, rj['data']['after'], hot_list)
