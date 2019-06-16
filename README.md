# Crowd Computing Assignment - Credibility Assessment :mortar_board:

Crowd computing assignment created using [Figure Eight](https://www.figure-eight.com/) for the crowdsourcing part and [scikit-learn](https://scikit-learn.org) for the Machine Learning part. This project is done for TU Delft's course Crowd Computing (CS4145) 2019.

## System Overview :green_book:

The system created within this assignment aims to predict the credibility of a given tweet. In particular, a batch of unlabeled tweets is first annotated via a crowdsourcing task to create a training set than can train a machine learning model. Following that, the trained model can predict the credibility of new unseen tweets. That said, the model's predictions can be mistaken. Therefore, a second crowdsourcing task was introduced which receives low confidence predictions by the model and tweets flagged as incorrectly labeled by Twitter users. These samples are re-annotated and forwarded on Twitter while the new labeled data can also be used to re-train the machine learning model, thus increasing its prediction accuracy.

<p align="center">
  <img src="https://github.com/psoilis/Crowd-Computing-Group-1/blob/master/images/TweetGuard.png" height="307" width="628">
</p>

### Crouwdsourcing Task #1

Explain things about task 1 and how we use it for the ML part. An example of our first annotation task is showcased in the image below. 

<p align="center">
  <img src="https://github.com/psoilis/Crowd-Computing-Group-1/blob/master/images/task1_example.PNG" height="380" width="628">
</p>


### Crouwdsourcing Task #2 

Explain things about task 2. An example of our second annotation task is showcased in the image below. 

<p align="center">
  <img src="https://github.com/psoilis/Crowd-Computing-Group-1/blob/master/images/task2_example.PNG" height="218" width="784">
</p>

### Machine Learning Task

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
