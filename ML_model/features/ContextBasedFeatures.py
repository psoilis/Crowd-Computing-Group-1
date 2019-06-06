from utils import utils

def has_url(post):
    return int(len(utils.extract_url(post['tweet_text'])) > 0)


def has_shortened_url(post):
    return int(utils.is_url_shortened(post['tweet_text']) > 0)


def has_emoji(post):
    return utils.has_emoji(post['tweet_text'])


def has_user_mention(post):
    return int(utils.number_of_user_mentions(post['tweet_text']) > 0)


def number_of_user_mentions(post):
    return utils.number_of_user_mentions(post['tweet_text'])


def number_of_hashtags(post):
    return utils.number_of_hashtags(post['tweet_text'])


def is_reply(post):
    return int(post['tweet_is_reply'])


def word_count(post):
    return utils.len_words(post['tweet_text'])


def char_count(post):
    return utils.len_characters(post['tweet_text'])


def get_sentiment_polarity_feature(post):
    """
    Calculates the compound score of the post's text and the
    article's title
    :param post: the current post
    :return: the compound score
    """
    return utils.get_tweets_sentiment(post['tweet_text'])


def punctuation_count(post):
    return utils.punctuation_count(post['tweet_text'])
