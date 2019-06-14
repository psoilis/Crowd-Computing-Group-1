from tqdm import tqdm
from random import randint
from utils import utils
import os
import json



def main():
    path_to_json = '/Users/psoilis/Documents/TU_Delft/Q4/Crowd_Computing/Group_Assignment_Dataset/march18_vaccine_twitter/'
    # Extracting all the json files from the directory
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    tweets = 0
    id_list = open("unique_tweet_ids.txt", "r").read()  # reading IDs of non retweeted tweets
    tweet_data = []
    for file in tqdm(json_files):
        with open(path_to_json + file, 'r') as f:
            data = json.load(f)
            for i in range(len(data)):
                # Skipping invalid entries with "limit"
                if data[i].get('limit') is not None:
                    print('Skipped')
                    continue
                if str(data[i]['id']) in id_list:
                    if 'retweeted_status' in data[i]:
                        # tweet_data.append(extract_info(data[i]['retweeted_status']))
                        # Filter out some of the truncated tweet texts
                        if data[i]['truncated'] == False:
                            tweets += 1
                            tweet_data.append(extract_info(data[i]['retweeted_status']))

    # Writing tweets to file
    with open('dataset_human_vaccination.json', 'w', encoding='utf8') as outputfile:
        json.dump(tweet_data, outputfile, ensure_ascii=False)

    print('Total number of tweets:', tweets)


def extract_info(data):
    tweet = {}
    tweet['tweet_id'] = data['id']
    tweet['tweet_created_at'] = utils.transform_date(data['created_at'])
    if 'extended_tweet' in data:
        tweet['tweet_text'] = data['extended_tweet']['full_text']
    else:
        tweet['tweet_text'] = data['text']
    if data['in_reply_to_status_id'] is not None or data['in_reply_to_status_id_str'] is not None or data['in_reply_to_user_id'] is not None\
            or data['in_reply_to_user_id_str'] is not None or data['in_reply_to_screen_name'] is not None:
        tweet['tweet_is_reply'] = True
    else:
        tweet['tweet_is_reply'] = False
    tweet['tweet_likes'] = data['favorite_count']
    tweet['tweet_retweets'] = data['retweet_count']
    tweet['tweet_replies'] = data['reply_count']
    tweet['tweet_quotes'] = data['quote_count']
    tweet['user_name'] = data['user']['name']
    tweet['user_twitter_handle'] = data['user']['screen_name']
    tweet['user_created_at'] = utils.transform_date(data['user']['created_at'])
    tweet['user_image'] = data['user']['profile_image_url']
    tweet['user_is_verified'] = data['user']['verified']
    tweet['user_followers'] = data['user']['followers_count']
    tweet['user_friends'] = data['user']['friends_count']
    tweet['label'] = randint(0, 1)
    return tweet


if __name__ == "__main__":
    main()
