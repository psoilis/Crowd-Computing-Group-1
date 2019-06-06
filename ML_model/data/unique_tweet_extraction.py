from tqdm import tqdm
import os
import json
from datetime import datetime


def main():
    # path_to_json = 'C:/Users/Panos/Downloads/march18_vaccine_twitter/'
    path_to_json = '/Users/psoilis/Documents/TU_Delft/Q4/Crowd_Computing/Group_Assignment_Dataset/newtweets/'
    # Extracting all the json files from the directory
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    english_tweets = 0
    tweets = 0
    unique_tweets = {}
    for file in tqdm(json_files):
        with open(path_to_json + file, 'r') as f:
            data = json.load(f)
            for i in range(len(data)):
                # Skipping invalid entries with "limit"
                if data[i].get('limit') is not None:
                    print('Skipped')
                    continue
                tweets += 1
                if data[i]['lang'] == 'en':
                    english_tweets += 1
                    unique_tweets = find_unique(data[i], unique_tweets)
    # Writing ids of unique non-retweeted tweets to file
    with open('unique_tweet_ids.txt', 'w') as file:
        for key, value in unique_tweets.items():
            file.write(str(value[0]) + '\n')
    print('Unique tweets:', len(unique_tweets))
    print('Total number of tweets:', tweets)
    print('English tweets:', english_tweets)


def find_unique(data, unique_tweets):
    if data['text'] not in unique_tweets.keys():
        unique_tweets[data['text']] = [data['id'], data['created_at']]
    else:
        new_tweet_timestamp = datetime.strptime(data['created_at'], '%a %b %d %H:%M:%S %z %Y')
        dict_tweet_timestamp = datetime.strptime(unique_tweets[data['text']][1], '%a %b %d %H:%M:%S %z %Y')
        if new_tweet_timestamp < dict_tweet_timestamp:
            unique_tweets[data['text']][0] = data['id']
            unique_tweets[data['text']][1] = data['created_at']
    return unique_tweets


if __name__ == "__main__":
    main()
