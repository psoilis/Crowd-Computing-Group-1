import csv
import json
from features import UserBasedFeatures as ubf
from features import ContextBasedFeatures as cbf


def main():
    with open('data/dataset_human_vaccination_subsample.json', 'r') as f:
        headers = False
        tweets = json.load(f)
        for i in range(len(tweets)):
            # Number of words
            tweet_len_words = cbf.word_count(tweets[i])
            # Number of characters
            tweet_len_chars = cbf.char_count(tweets[i])
            # Punctuation count
            tweet_punc_count = cbf.punctuation_count(tweets[i])
            # Tweet contains URL (binary)
            tweet_has_url = cbf.has_url(tweets[i])
            # Tweet contains shortened URL (binary)
            tweet_has_short_url = cbf.has_shortened_url(tweets[i])
            # Tweet contains emoji
            tweet_has_emoji = cbf.has_emoji(tweets[i])
            # Tweet has user mentions
            tweet_has_mentions = cbf.has_user_mention(tweets[i])
            # Number of user mentions
            tweet_num_mentions = cbf.number_of_user_mentions(tweets[i])
            # Number of hashtags
            tweet_num_hashtags = cbf.number_of_hashtags(tweets[i])
            # Number of likes
            tweet_num_likes = cbf.number_of_likes(tweets[i])
            # Number of retweets
            tweet_num_retweets = cbf.number_of_retweets(tweets[i])
            # Number of replies
            tweet_num_replies = cbf.number_of_replies(tweets[i])
            # Tweet compound score (sentiment)
            tweet_sentiment = cbf.get_sentiment_polarity_feature(tweets[i])
            # Tweet is a reply to another tweet
            tweet_is_reply = cbf.is_reply(tweets[i])
            # User time on Twitter
            user_time = ubf.time_on_twitter(tweets[i])
            # User number of followers
            user_followers = ubf.number_of_followers(tweets[i])
            # User number of friends
            user_friends = ubf.number_of_followers(tweets[i])
            # User is verified
            user_is_verified = ubf.is_verified(tweets[i])
            # User handle contains numbers (binary)
            user_handle_has_number = ubf.handle_contains_numbers(tweets[i])

            # Writing line to file (could write them in batches to improve performance)
            feature_output = str(tweets[i]['tweet_id']) + ',' + str(tweets[i]['label']) + ',' + str(tweet_len_words) \
                             + ',' + str(tweet_len_chars) + ',' + str(tweet_punc_count) + ',' + str(tweet_has_url) \
                             + ',' + str(tweet_has_short_url) + ',' + str(tweet_has_emoji) + ',' + str(tweet_has_mentions) \
                             + ',' + str(tweet_num_mentions) + ',' + str(tweet_num_hashtags) + ',' + str(tweet_num_likes) \
                             + ',' + str(tweet_num_retweets) + ',' + str(tweet_num_replies) + ',' + str(tweet_sentiment) \
                             + ',' + str(tweet_is_reply) + ',' + str(user_time) + ',' + str(user_followers) + ',' + str(user_friends)\
                             + ',' + str(user_is_verified) + ',' + str(user_handle_has_number)
            # If first sample, write the file headers first
            if not headers:
                feature_headers = 'Tweet_ID,Label,Tweet_Length_Words,Tweet_Length_Chars,Tweet_Punctuation_Count'\
                                  ',Tweet_Has_URL,Tweet_Has_Short_URL,Tweet_Has_Emoji,Tweet_Has_User_Mentions,Tweet_Num_Mentions'\
                                  ',Tweet_Num_Hashtags,Tweet_Num_Likes,Tweet_Num_Retweets,Tweet_Num_Replies,Tweet_Compound_Score'\
                                  ',Tweet_Is_Reply,User_Time_on_Twitter,User_Followers,User_Friends,User_Is_Verified,User_Handle_Has_Number'
                # Writing file headlines
                with open('data/features.csv', encoding='utf8', mode='w',
                          newline='') as features_file:
                    features_writer = csv.writer(features_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    features_writer.writerow([feature_headers])
                headers = True

            with open('data/features.csv', encoding='utf8', mode='a', newline='') as features_file:
                features_writer = csv.writer(features_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                features_writer.writerow([feature_output])


if __name__ == '__main__':
    main()
