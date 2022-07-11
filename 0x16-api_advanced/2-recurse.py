#!/usr/bin/python3
"""Get hot posts from reddit sub."""


import requests


def recurse(subreddit, after='', hot_list=[]):
    """Get posts of sub."""
    headers = {'User-Agent': "Mozilla/5.0"}
    url = 'https://www.reddit.com'
    res = requests.get(f'{url}/r/{subreddit}/hot.json?after={after}',
                       headers=headers, allow_redirects=False)
    if res.status_code == 302:
        return None
    rj = res.json()
    if rj.get('data') is None:
        return None
    for post in rj['data']['children']:
        title = post['data']['title']
        hot_list.append(title)
    if rj['data']['after'] is None:
        return hot_list
    return recurse(subreddit, rj['data']['after'], hot_list)
