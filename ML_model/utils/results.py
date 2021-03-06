import json_lines
import csv


def parse_json(input_file, output_file):
    with open(output_file, encoding='utf8', mode='w',
              newline='') as features_file:
        features_writer = csv.writer(features_file, delimiter=',', quotechar='', quoting=csv.QUOTE_NONE)
        features_writer.writerow(['Tweet_ID', 'Crowd_Label'])
        with open(input_file, 'rb') as f:
            for tweet_result in json_lines.reader(f):
                # Credible tweets
                if tweet_result['results']['sentiment']['agg'] == 'definetly_credible' \
                        or tweet_result['results']['sentiment']['agg'] == 'seems_credible':
                    features_writer.writerow([tweet_result['data']['tweet_id'], 1])
                # Not credible tweets
                elif tweet_result['results']['sentiment']['agg'] == 'definitely_not_credible':
                    features_writer.writerow([tweet_result['data']['tweet_id'], 0])
                # Skipping cannot decide and none
                else:
                    continue
