from tqdm import tqdm
import os, json


def main():
    path_to_json = 'C:/Users/Panos/Downloads/march18_vaccine_twitter/'
    # Extracting all the json files from the directory
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    english_tweets = 0
    tweets = 0
    positive_bias_tweets = 0
    negative_bias_tweets = 0
    tweet_data = []
    for file in tqdm(json_files):
        with open(path_to_json + file, 'r') as f:
            data = json.load(f)
            for i in range(100):
                # Skipping invalid entries with "limit"
                if data[i].get('limit') is not None:
                    print('Skipped')
                    continue
                tweets += 1
                try:
                    if data[i]['lang'] == 'en':
                        english_tweets += 1
                        tweet_data.append(extract_info(data[i]))
                        # tweet_data = extract_info(data)
                        # if '#vaccineswork' in data[i]['text'] or 'vaccines work' in data[i]['text']:
                        #     print(data[i]['text'], data[i]['id'], file)
                        #     positive_bias_tweets += 1
                        # if '#antivax' in data[i]['text'] or 'antivax' in data[i]['text']:
                        #     negative_bias_tweets += 1
                except:
                    print(data[i], file)
                    exit()
    # Writing tweets to file
    with open('C:/Users/Panos/Downloads/dataset_human_vaccination.json', 'w',
              encoding='utf8') as outputfile:
        json.dump(tweet_data, outputfile, ensure_ascii=False)

    print('Total number of tweets:', tweets)
    print('English tweets:', english_tweets)
    print('Positively biased tweets:', positive_bias_tweets)
    print('Negatively biased tweets:', negative_bias_tweets)


def extract_info(data):
    tweet = {}
    tweet['tweet_id'] = data['id']
    tweet['tweet_created_at'] = data['created_at']
    tweet['tweet_text'] = data['text']
    # If one of the five in_reply_to fields is not null
    if data['in_reply_to_status_id'] is not None or data['in_reply_to_status_id_str'] is not None or data['in_reply_to_user_id'] is not None\
            or data['in_reply_to_user_id_str'] is not None or data['in_reply_to_screen_name'] is not None:
        tweet['tweet_is_reply'] = True
    else:
        tweet['tweet_is_reply'] = False
    tweet['user_twitter_handle'] = data['user']['screen_name']
    tweet['user_created_at'] = data['user']['created_at']
    tweet['user_is_verified'] = data['user']['verified']
    tweet['user_followers'] = data['user']['followers_count']
    tweet['user_friends'] = data['user']['friends_count']
    return tweet


if __name__ == "__main__":
    main()