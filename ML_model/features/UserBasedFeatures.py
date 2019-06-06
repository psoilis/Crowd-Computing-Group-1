from utils import utils


def time_on_twitter(post):
    """
    Calculates the users time on twitter in months
    :param post: the current post
    :return: an integer that measures the months rounded up
    """
    return utils.time_on_twitter(post['user_created_at'])


def number_of_followers(post):
    return post['user_followers']


def number_of_friends(post):
    return post['user_friends']


def is_verified(post):
    return int(post['user_is_verified'])


def handle_contains_numbers(post):
    return int(any(char.isdigit() for char in post['user_twitter_handle']))
