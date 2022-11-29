#!/usr/bin/python3
"""
This is a function that queries the Reddit API and returns the number of subscribers 
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers (not active users, total subscribers) 
    for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
    v1.0.0 (by /u/fraol21)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
