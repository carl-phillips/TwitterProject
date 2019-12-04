from django.db import models

"""
Class Tweet
This holds information for the Tweets received.
"""
class Tweet:
    def __init__(self, url, user_name, text, created_at, hashtags, retweet_count=0, favorite_count=0):
        try:
            self.url = url
        except TypeError:
            TweetCreationException(TypeError)
        try:
            self.hashtags = hashtags
        except TypeError:
            TweetCreationException(TypeError)
        try:
            self.user_name = user_name
        except TypeError:
            TweetCreationException(TypeError)
        try:
            self.text = text
        except TypeError:
            TweetCreationException(TypeError)
        try:
            self.created_at = created_at
        except TypeError:
            TweetCreationException(TypeError)
        self.retweet_count = retweet_count
        self.favorite_count = favorite_count

    def __str__(self):
        return 'Tweet from User: ' + str(self.user_name) + ' - Said: \"' + str(self.text) + '\" - Created at: ' + str(self.created_at) + ' - Favorite Count: ' + str(self.favorite_count) + ' - Retweet Count: ' + str(self.retweet_count) + ' - Hashtags: ' + str(self.hashtags)

    def __repr__(self):
        return 'Tweet from user_name: ' + str(self.user_name) + '\ntext: \"' + str(self.text) + '\"\ncreated_at: ' + str(self.created_at) + '\nfavorite_count: ' + str(self.favorite_count) + '\nretweet_count: ' + str(self.retweet_count) + '\nhashtags: ' + str(self.hashtags)

    def display(self):
        return 'Tweet from User: ' + str(self.user_name) + ' - Said: \"' + str(self.text) + '\" - Created at: ' + str(self.created_at) + ' - Favorite Count: ' + str(self.favorite_count) + ' - Retweet Count: ' + str(self.retweet_count) + ' - Hashtags: ' + str(self.hashtags)


def TweetCreationException(TypeError):
    print("Big error" + TypeError)
    pass

"""class defined for database model"""
# class Tweets(models.Model):
#     hashtags = models.CharField(max_length=250)
#     retweet_count = models.IntegerField(default=0)
#     favorite_count = models.IntegerField(default=0)
#     user_name = models.CharField(max_length=50)
#     text = models.CharField(max_length=250)
#     created_at = models.DateTimeField('date picked')
#
#     def __str__(self):
#         return 'Tweet from User: ' + str(self.user_name) + ' - Said: \"' + str(self.text) + '\" - Created at: ' + str(self.created_at) + ' - Favorite Count: ' + str(self.favorite_count) + ' - Retweet Count: ' + str(self.retweet_count) + ' - Hashtags: ' + str(self.hashtags)
#
#     def __repr__(self):
#         return 'Tweet from user_name: ' + str(self.user_name) + '\ntext: \"' + str(self.text) + '\"\ncreated_at: ' + str(self.created_at) + '\nfavorite_count: ' + str(self.favorite_count) + '\nretweet_count: ' + str(self.retweet_count) + '\nhashtags: ' + str(self.hashtags)
#
#     def display(self):
#         return 'Tweet from User: ' + str(self.user_name) + ' - Said: \"' + str(self.text) + '\" - Created at: ' + str(self.created_at) + ' - Favorite Count: ' + str(self.favorite_count) + ' - Retweet Count: ' + str(self.retweet_count) + ' - Hashtags: ' + str(self.hashtags)
