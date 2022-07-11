#!/usr/bin/python3
"""Get subs from reddit."""
import requests


def top_ten(subreddit):
    """Get number of subs."""
    headers = {'User-Agent': "Mozilla/5.0"}
    url = 'https://www.reddit.com'
    res = requests.get(f'{url}/r/{subreddit}/hot.json?limit=10',
                       headers=headers, allow_redirects=False)
    if res.status_code == 302:
        print('None')
        return
    rj = res.json()
    if rj.get('data') is None:
        print('None')
        return
    for post in rj['data']['children']:
        title = post['data']['title']
        print(title)
