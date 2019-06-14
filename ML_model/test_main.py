from features.UserBasedFeatures import time_on_twitter, number_of_followers, number_of_friends, is_verified, \
    handle_contains_numbers
from features.ContextBasedFeatures import has_url, has_shortened_url, has_emoji, has_user_mention, \
    number_of_user_mentions, number_of_hashtags, word_count, char_count, get_sentiment_polarity_feature,\
    punctuation_count
from utils import utils
import json
from classification import RandomForest, NaiveBayes, MaximumEntropy, XGBoost
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


input_file = open('data/dataset_human_vaccination.json', encoding="utf8")
json_array = json.load(input_file)

# Feature extraction
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


# test classifiers with confidence output -> -1 for uncertain 0 for (class 1) 1 for (class 2)
RANDOM_STATE = 123

X, y = make_classification(n_samples=500, n_features=25,
                           n_clusters_per_class=1, n_informative=15,
                           random_state=RANDOM_STATE)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

rf = RandomForest.RandomForest()

rf.train(x_train=X_train, y_train=y_train)

print(rf.predict_with_confidence(data=X_test, confidence=0.1))

xgb = XGBoost.XGBoost()
xgb.train(x_train=X_train, y_train=y_train)

print(xgb.predict_with_confidence(data=X_test, confidence=0.1))

nb = NaiveBayes.NaiveBayes()
nb.train(x_train=X_train, y_train=y_train)

print(nb.predict_with_confidence(data=X_test, confidence=0.1))

me = MaximumEntropy.MaximumEntropy()
me.train(x_train=X_train, y_train=y_train)

print(me.predict_with_confidence(data=X_test, confidence=0.1))


date = "Tue Mar 07 04:00:17 +0000 2017"

print(utils.transform_user_date(date))

print(utils.transform_tweet_date(date))
