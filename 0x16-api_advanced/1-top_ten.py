#!/usr/bin/python3
""" Top Ten """


import requests


def top_ten(subreddit):
    """
    script to show the first 10 posts of the reddit api
    """

    endpoint = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user = {'User-Agent': 'gerardomp18'}
    response = requests.get(endpoint, headers=user,
                            allow_redirects=False,
                            params={'limit': '10'})

    if response.status_code == 200:
        listPost = response.json().get('data').get('children')
        for post in listPost:
            print(post.get('data').get('title'))
    print(None)
