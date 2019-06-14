from tqdm import tqdm
import json


def main():
    positive_bias_tweets = 0
    tweet_data = []
    with open('dataset_human_vaccination.json', 'r') as f:
        data = json.load(f)
        for i in range(len(data)):
            # Filters 743 tweets. Sub-sampleed 406 to maintain a 50-50 balance
            if '#vaccineswork' in data[i]['tweet_text']:
                positive_bias_tweets += 1
                if positive_bias_tweets <= 406:
                    tweet_data.append(data[i])

            # Filters 406 tweets
            if 'antivax' in data[i]['tweet_text'] or 'anti-vax' in data[i]['tweet_text']:
                tweet_data.append(data[i])

    # Writing final subsampled tweets to file
    with open('dataset_human_vaccination_subsample.json', 'w', encoding='utf8') as outputfile:
        json.dump(tweet_data, outputfile, ensure_ascii=False)


if __name__ == "__main__":
    main()
