# Crowd Computing Assignment - Credibility Assessment :mortar_board:

Crowd computing assignment created using [Figure Eight](https://www.figure-eight.com/) for the crowdsourcing part and [scikit-learn](https://scikit-learn.org) for the Machine Learning part. This project is done for TU Delft's course Crowd Computing (CS4145) 2019.

## System Overview :green_book:

The system created within this assignment aims to predict the credibility of a tweet about human vaccination. In particular, a batch of unlabeled tweets is first annotated via a crowdsourcing task to create a training set than can train a machine learning model. Following that, the trained model can predict the credibility of new unseen tweets. That said, the model's predictions can be mistaken. Therefore, a second crowdsourcing task was introduced which receives low confidence predictions by the model and tweets flagged as incorrectly labeled by Twitter users. These samples are re-annotated and forwarded on Twitter while the new labeled data can also be used to re-train the machine learning model, thus increasing its prediction accuracy. An overivew of the proposed pipeline can be found in the graph below.

<p align="center">
  <img src="https://github.com/psoilis/Crowd-Computing-Group-1/blob/master/images/TweetGuard.png" height="307" width="628">
</p>

### Crouwdsourcing Task #1

This task refers to the annotation of the unlabeled batch which is to be used as a training set for the machine learning model. The worker is required to answer three questions:
1. Validate whether the tweet contains information about human vaccination or not.
2. Annotate the tweet with regard to its credibility.
3. Provide reasoning behind the factors that influenced his or her annotation.

<p align="center">
  <img src="https://github.com/psoilis/Crowd-Computing-Group-1/blob/master/images/task1_example.PNG" height="380" width="628">
</p>


### Crouwdsourcing Task #2 

This task corresponds to the tweets that need to be re-annotated. The worker answers two questions:
1. Whether the tweet contains information about human vaccination or not.
2. He or she is provided with the predicted annotation of the model and has to specify whether they agree with it or not.

<p align="center">
  <img src="https://github.com/psoilis/Crowd-Computing-Group-1/blob/master/images/task2_example.PNG" height="218" width="784">
</p>

### Machine Learning Part

For the Machine Learning part, we selected the [Maximum Entropy](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) classifier because it has proven to work well in similar applications. Moreover, we decided to make this classification task binary by merging the 'seems credible' and 'definitely credible' annotations into one class 'credible'(1 in the .csv files) and the 'definitely not credible' in another 'not credible'(0 in the .csv files). In addition, we tailored the model to work with confidence input. By that, we mean that if the difference between the two class probabilities is smaller than the confidence we assume that this judgment is with low confidence and give it as input to our second crowdsourcing task. However, since the budget/time was limited we did not have enough labeled data for meaningful results. Furthermore, due to the previously stated situation, further exploration into a better Machine Learning pipeline was limited. The Machine Learning pipeline is showcased below.
 
 <p align="center">
  <img src="https://github.com/psoilis/Crowd-Computing-Group-1/blob/master/images/ML_pipeline.png" height="223" width="650">
</p>
 
## Setup :computer:

### Figure Eight
* Create a user account on [Figure Eight](https://make.figure-eight.com/jobs)
* Upload data from `Figure_Eight/data/figure8_dataset.xlsx`
* Copy code from `Figure_Eight/initial/` for CML, CSS and Javascript under "Design" tab
* Change name of the task
* Change "Rows Per Page" to 5 under "Settings -> Pay"
* Create Honeypot Questions under "Quality" tab
* Change minimum time per page to 60s under "Settings -> Quality Control -> Quality Control Settings"
* Change minimum accuracy for Test questions to 60% under "Settings -> Quality Control -> Test Questions"
* Navigate to "Launch" tab and change Judgments per Row
* Launch job  
  
  
* Repeat for low confidence task, except do not upload data. Also, take CML, CSS and Javascript code
from `Figure_Eight/low_confidence/` this time.

### Machine Learning Pipeline

A detailed example on how to run the entire pipeline is located in `ML_Model/pipeline.py` and is showcased below.


```python
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
```

#### Parsing Figure Eight's Output
In order to parse Figure Eight's Output we created a Python script located in `ML_Model/utils/results.py` that takes two parameters, the location of the Figure Eight's output as the input file and the location that we want to write the merged file.

#### Machine Learning Classifiers 
The code we developed for the classification with confidence using the Maximum Entropy classifier is located in `ML_Model/classification/MaximumEntropy.py` and is a Python class that has two main functions `train` for taraining the model and `predict_with_confidence` that gives spredictions based on the given confidence level.

#### JSON to XLSX 
An other addition is that Figure8 wants the data in XLSX format so we created a script that transforms the JSON file that we get from Twitter's API into the required XLSX format in `ML_Model/utils/from_JSON_to_XLSX.py`


## Team members :busts_in_silhouette:

[Stavrangelos Gamvrinos](https://github.com/agamvrinos)

[Jody Liu](https://github.com/jdyli)

[Kyriakos Psarakis](https://github.com/kPsarakis)

[Hendrig Sellik](https://github.com/hsellik) 

[Panagiotis Soilis](https://github.com/psoilis)
