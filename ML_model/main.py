import csv
import json
from utils import utils
from random import randint
from features import UserBasedFeatures as ubf
from features import ContextBasedFeatures as cbf


def main():
    with open('data/dataset_human_vaccination_subsample.json', 'r') as f:
        headers = False
        count = 0  # elements processed
        tweets = json.load(f)
        for i in range(len(tweets)):
            count += 1
            print('Sample', count)
            print('Time on Twitter: ', ubf.time_on_twitter(tweets[i]))
            print('Number of followers: ', ubf.number_of_followers(tweets[i]))
            print('Number of friends: ', ubf.number_of_friends(tweets[i]))
            print('Is user verified: ', ubf.is_verified(tweets[i]))
            print('Does the handle contain numbers: ', ubf.handle_contains_numbers(tweets[i]))
            print('Url: ', cbf.has_url(tweets[i]))
            print('Shortened url : ', cbf.has_shortened_url(tweets[i]))
            print('Has emoji: ', cbf.has_emoji(tweets[i]))
            print('Has user mention: ', cbf.has_user_mention(tweets[i]))
            print('Number of user mentions: ', cbf.number_of_user_mentions(tweets[i]))
            print('Number of hashtags: ', cbf.number_of_hashtags(tweets[i]))
            print('Number of words: ', cbf.word_count(tweets[i]))
            print('Number of characters: ', cbf.char_count(tweets[i]))
            print('Punctuation count: ', cbf.punctuation_count(tweets[i]))
            print('Tweets sentiment: ', cbf.get_sentiment_polarity_feature(tweets[i]))
            # tweets[i]
            # # Reading tweets[i]/article elements
            # tweets[i]_id = utils.tweets[i]_id(tweets[i])
            # tweets[i]_title = utils.title(tweets[i])
            # article_title = utils.article(tweets[i])
            # # Extracting sample label
            # tweets[i]_label = randint(0, 1)
            # # Presence of image in a tweets[i]
            # has_image = imf.image_presence(tweets[i])
            # 
            # # Writing line to file (could write them in batches to improve performance)
            # feature_output = tweets[i]_id + ',' + str(tweets[i]_label) + ',' + str(has_image) + ',' + str(tweets[i]_creation_hour)
            # # If first sample, write the file headers first
            # if not headers:
            #     feature_headers = 'tweets[i]_ID,Label,Has_Img,tweets[i]_Creation_Hour,tweets[i]_Title_Begins_With_Interrogative,' \
            #                       'Article_Title_Begins_With_Interrogative,tweets[i]_Title_Begins_With_Number'
            #     # Writing file headlines
            #     with open('dataset/features.csv', encoding='utf8', mode='w',
            #               newline='') as features_file:
            #         features_writer = csv.writer(features_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #         features_writer.writerow([feature_headers])
            #     headers = True
            # with open('dataset/features.csv', encoding='utf8', mode='a', newline='') as features_file:
            #     features_writer = csv.writer(features_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #     features_writer.writerow([feature_output])


if __name__ == '__main__':
    main()

# import pandas as pd
# from classification import NaiveBayes
# from classification import MaximumEntropy
# from classification import RandomForest
# from classification import XGBoost as xgb
#
# files = [
#     # "final_feature_vectors_20.csv",
#     # "final_feature_vectors_40.csv",
#     # "final_feature_vectors_60.csv",
#     # "final_feature_vectors_80.csv",
#     # "final_feature_vectors_120.csv",
#     "final_feature_vectors_160.csv",
#     # "final_feature_vectors_200.csv",
#     # "features_no_ngrams.csv",
# ]
#
# me = MaximumEntropy.MaximumEntropy()
# nb = NaiveBayes.NaiveBayes()
# rf = RandomForest.RandomForest()
# xg = xgb.XGBoost()
#
# for file in files:
#     df = pd.read_csv("dataset/" + file)
#     X = df.loc[:, ~df.columns.isin(['Label', 'tweets[i]_ID'])].values
#     y = df['Label'].values
#
#     nb.train(X, y)
#     # results = nb.cross_validation(X, y)
#     # print(results)
#
#     me.train(X, y)
#     # print(svm.cross_validation(X, y))
#     # svm.optimize_params(X, y)
#
#     # rf = RandomForest.RandomForest()
#     # rf.train(X, y)
#     # print(rf.cross_validation(X, y))
#
#     rf.train(X, y)
#
#     xg.train(X, y)
#
#
# df = pd.read_csv("dataset/leftout_test.csv")
# X = df.loc[:, ~df.columns.isin(['Label', 'tweets[i]_ID'])].values
# y = df['Label'].values
#
# print(nb.predict(X, y, True))
# print(me.predict(X, y, True))
# print(rf.predict(X, y, True))
# print(xg.predict(X, y, True))
