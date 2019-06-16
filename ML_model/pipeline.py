from classification import MaximumEntropy
from sklearn.model_selection import train_test_split
import pandas as pd
from utils import merge_figure8_with_extracted_features as mf
from utils import results as res
from features import feature_export as ex


# Extract the features from the sub-sampled tweets that contain the search parameters that we want
ex.feature_export(input_file='data/dataset_human_vaccination_subsample.json', output_file='data/features.csv')

# Extract the labels from the Figure8's job file
res.parse_json(input_file='data/job_1394060.json', output_file='data/crowd_annotations.csv')

# Read both the feature and label files
df = mf.merge_figure8_with_extracted_features('data/features.csv', 'data/crowd_annotations.csv')

# Get the feature vector with the tweet's id
X = df.loc[:, ~df.columns.isin(['Crowd_Label'])].values

# Get the labels
y = df['Crowd_Label'].values

# Classification example with 80% train 20% test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Get the feature vectors without the tweet's id
X_train_without_id = X_train[:, 1:-1]
X_test_without_id = X_test[:, 1:-1]

# Test classifiers with confidence output tuple (confidence, judgment) confidence -> 0 (low confidence), 1 (high)
#                                                                      judgment -> 0 (not credible), 1 (credible)
me = MaximumEntropy.MaximumEntropy()

# Train the classifier
me.train(x_train=X_train_without_id, y_train=y_train)

# Get the predictions with confidence
results = pd.DataFrame(me.predict_with_confidence(data=X_test_without_id, confidence=0.1))

# Get the tweet ids
ids = pd.DataFrame(X_test[:, 0], dtype='int64')

# Merge the results and ids to have the final output
output = pd.concat([ids, results], axis=1)
output.columns = ['Tweet_ID', 'Confidence', 'Prediction']

# Write the low and high confidence predictions in different files
low_confidence = output.loc[output['Confidence'] == 0]
high_confidence = output.loc[output['Confidence'] == 1]

low_confidence.loc[:, ~low_confidence.columns.isin(['Confidence'])]\
    .to_csv('data/classification_output_low_confidence.csv', index=False)
high_confidence.loc[:, ~high_confidence.columns.isin(['Confidence'])]\
    .to_csv('data/classification_output_high_confidence.csv', index=False)
