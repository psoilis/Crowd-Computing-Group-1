from datetime import datetime
import math
import re
import emoji
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import string

analyser = SentimentIntensityAnalyzer()


def time_on_twitter(user_signup_date):
    d1 = datetime.strptime(datetime.strptime(user_signup_date, '%d-%m-%Y').strftime('%Y-%m-%d'), '%Y-%m-%d')
    d2 = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
    return math.ceil((abs((d1 - d2).days)/30.44))


def extract_url(content):

    extracted = re.findall("(?P<url>https?://[^\s]+)", content)

    if extracted is not None:
        return extracted
    return None


def is_url_shortened(content):
    extracted = extract_url(content)
    c = 0
    for url in extracted:
        if (re.findall("https?: // t\.co /\S +",url) is not None) or \
                (re.findall("https?: // bit\.ly /\S +",url) is not None) or \
                (re.findall("https?: // goo\.gl /\S +",url) is not None):
            c += 1
    return c


def has_emoji(content):
    for c in content:
        if c in emoji.UNICODE_EMOJI:
            return 1
    return 0


def number_of_user_mentions(content):

    count = 0

    for c in content:
        if "@" in c:
            count += 1

    return count


def number_of_hashtags(content):

    count = 0

    for c in content:
        if "#" in c:
            count += 1

    return count


def len_characters(content):
    # returns the content's number of characters (-1 if empty)
    chars_len = - 1
    if len(content) != 0:
        if isinstance(content, list):
            # list case
            chars_sum = 0
            for element in content:
                chars_sum = chars_sum + len(element)
            chars_len = chars_sum / float(len(content))
        else:
            # string case
            chars_len = len(content)

    return chars_len if chars_len != 0 else -1


def len_words(content):
    # returns the content's number of words (-1 if empty)
    words_len = - 1
    if len(content) != 0:
        if isinstance(content, list):
            # list case
            words_sum = 0
            for element in content:
                words = element.split(" ")
                words_sum = words_sum + len(words)
                words_len = words_sum / float(len(content))
        else:
            # string case
            words = content.split(" ")
            words_len = len(words)
    return words_len if words_len != 0 else -1


def get_tweets_sentiment(content):
    return analyser.polarity_scores(content)


def punctuation_count(content):
    count = 0
    for c in content:
        if c in string.punctuation:
            count += 1
    return count


def transform_date(date):
    return datetime.strptime(date, '%a %b %d %H:%M:%S %z %Y').strftime('%d-%m-%Y')
