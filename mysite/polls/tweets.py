import twitter
import tkinter
from .tweet import Tweet
import datetime
import json

"""
Function to get tweets from twitter
Returns them in a tweets dict
"""
def get_tweets(search_string, result_type, time_range):

    api = twitter.Api(consumer_key='7SVoyHlwYgm90Y5HSzmTzUQ9O',
                      consumer_secret='D0crcrKca9S3TXuqGRPYhzBN0LJut34MecER8Ly8fb3xrM0Gja',
                      access_token_key='1199488399238926336-1jV9xq8bs4zdP5qiq96cUwP5GF1Fuz',
                      access_token_secret='71hibaH8BPkPwCytm5CH9N4RJonaRCrSKUqG9y3dwo2Ix')

    tweets = {}
    search = "q=" + str(search_string) + "%20&result_type=" + str(result_type) + "&since=" + str(time_range) + "&count=100";
    print(search)
    results = api.GetSearch(raw_query=search)
    i = 0
    for result in results:
        json_result = json.loads(str(result))
        t = Tweet(json_result['user']['profile_image_url'], json_result['user']['name'], json_result['text'], json_result['created_at'], json_result['hashtags'])
        if 'retweet_count' in json_result:
            t.retweet_count = json_result['retweet_count']
        if 'favorite_count' in json_result:
            t.favorite_count = json_result['favorite_count']
        tweets[i] = t
        i += 1

    return tweets
