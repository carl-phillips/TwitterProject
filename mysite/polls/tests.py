from django.test import TestCase

# Create your tests here.
import unittest
from unittest.mock import patch
from mysite.polls.tweet import TweetCreationException
from mysite.polls.tweet import Tweet

class TestSet(unittest.TestCase):
    def test_tweet_creation_basic(self):
        with self.assertRaises(TweetCreationException):
            t = Tweet("www.url.com", "user", "Text string", "hashtags")

    def test_tweet_creation(self):
        self.assertTrue(Tweet("www.url.com", "user", "Text string", "hashtags", 0, 0))

    def test_tweet_creation_fail(self):
        with self.assertRaises(ValueError):
            t = Tweet()


if __name__ == '__main__':
    unittest.main()