from features.UserBasedFeatures import time_on_twitter, number_of_followers, number_of_friends, is_verified, \
    handle_contains_numbers
from features.ContextBasedFeatures import has_url, has_shortened_url, has_emoji, has_user_mention, \
    number_of_user_mentions, number_of_hashtags, word_count, char_count, get_sentiment_polarity_feature,\
    punctuation_count
import json

# "user_created_at"


input_file = open('data/dataset_human_vaccination.json', encoding="utf8")
json_array = json.load(input_file)


for post in json_array:
    print('Time on Twitter: ', time_on_twitter(post))
    print('Number of followers: ', number_of_followers(post))
    print('Number of friends: ', number_of_friends(post))
    print('Is user verified: ', is_verified(post))
    print('Does the handle contain numbers: ', handle_contains_numbers(post))
    print('Url: ', has_url(post))
    print('Shortened url : ', has_shortened_url(post))
    print('Has emoji: ', has_emoji(post))
    print('Has user mention: ', has_user_mention(post))
    print('Number of user mentions: ', number_of_user_mentions(post))
    print('Number of hashtags: ', number_of_hashtags(post))
    print('Number of words: ', word_count(post))
    print('Number of characters: ', char_count(post))
    print('Punctuation count: ', punctuation_count(post))
    print('Tweets sentiment: ', get_sentiment_polarity_feature(post))
