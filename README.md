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

For the Machine Learning part, we selected the [Maximum Entropy](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) classifier because it has proven to work well in similar applications. Moreover, we decided to make this classification task binary by merging the 'seems credible' and 'definitely credible' annotations into one class 'credible'(1 in the .csv files) and the 'definitely not credible' in another 'not credible'(0 in the .csv files). In addition, we tailored the model to work with confidence input. By that, we mean that if the difference between the two class probabilities is smaller than the confidence we assume that this judgment is with low confidence and give it as input to our second crowdsourcing task. However, since the budget/time was limited we did not have enough labeled data for meaningful results. Furthermore, due to the previously stated situation, further exploration into a better Machine Learning pipeline was limited.
 
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

### Parsing Figure Eight's Output

### Machine Learning Classifiers 

### Pasing the Classification output for the second task




## Team members :busts_in_silhouette:

[Stavrangelos Gamvrinos](https://github.com/agamvrinos)

[Jody Liu](https://github.com/jdyli)

[Kyriakos Psarakis](https://github.com/kPsarakis)

[Hendrig Sellik](https://github.com/hsellik) 

[Panagiotis Soilis](https://github.com/psoilis)
