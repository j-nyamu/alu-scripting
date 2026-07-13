#!/usr/bin/python3
"""Recursively count keyword occurrences in hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Print a sorted count of keywords found in hot post titles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced-bot/1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0) + title.count(key)
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    sorted_counts = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))
            