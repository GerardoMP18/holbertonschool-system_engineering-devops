#!/usr/bin/python3
"""  How many subs? """


import requests


def number_of_subscribers(subreddit):
    """
    function to get the number of subreddit subscribers
    """

    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user = {'User-Agent': 'gerardomp18'}
    response = requests.get(endpoint, headers=user, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
