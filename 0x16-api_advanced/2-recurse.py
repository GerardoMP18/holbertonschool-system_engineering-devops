#!/usr/bin/python3
""" """


from asyncio import constants
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None
    """

    endpoint = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user = {'User-Agent': 'gerardomp18'}
    response = requests.get(endpoint, headers=user,
                            allow_redirects=False,
                            params={'after': after})

    if response.status_code == 200:
        after = response.json().get('data').get('after')

        listPost = response.json().get('data').get('children')
        for post in listPost:
            hot_list.append(post.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
