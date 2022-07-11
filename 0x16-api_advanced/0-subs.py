#!/usr/bin/python3
"""Get subs from reddit."""
import requests


def number_of_subscribers(subreddit):
    """Get number of subs."""
    headers = {'User-Agent': "Mozilla/5.0"}
    res = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                       headers=headers, allow_redirects=False)
    if res.status_code == 302:
        return 0
    rj = res.json()
    try:
        subs = rj['data']['subscribers']
    except Exception:
        return 0
    return subs
