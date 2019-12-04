import unittest
from unittest.mock import patch
from ..polls.tweet import Tweet
from ..polls.tweet import TweetCreationException

class TestTweet(unittest.TestCase):
    def test_tweet_creation_basic(self):
        self.assertTrue(Tweet("www.url.com", "user", "Text string", "date", "hashtags"))

    def test_tweet_creation(self):
        self.assertTrue(Tweet("www.url.com", "user", "Text string", "hashtags", 0, 0))

    def test_tweet_creation_fail(self):
        with self.assertRaises(TypeError):
            Tweet('F')


if __name__ == '__main__':
    unittest.main()