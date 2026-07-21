#!/usr/bin/python3
"""
1-top_ten module

Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:top_ten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])
    for post in data:
        print(post.get("data", {}).get("title"))