from sklearn.linear_model import LogisticRegression


class MaximumEntropy:
    """
    Class containing the functionality of the MaximumEntropy classifier
    """

    model = None

    def __init__(self):
        """
        The class constructor with the optimal hyper-parameters
        """
        self.model = LogisticRegression(solver='liblinear', C=1, penalty="l2")

    def train(self, x_train, y_train):
        """
        Function that trains the classifier

        :arg x_train: Training feature vectors
        :arg y_train: Training labels
         """
        self.model = self.model.fit(x_train, y_train)

    @staticmethod
    def choose_class():
        """
        Function that makes a choice between the two classes
        """
        return lambda r: 0 if r[0] > r[1] else 1

    def predict_with_confidence(self, data, confidence):
        """
        Function that trains the classifier
        :arg data: The feature vectors that we want to make a prediction on
        :arg confidence: the confidence threshold
        """
        return list(map(lambda p: (0, self.choose_class()(p)) if abs(p[0]-p[1]) < confidence else
                    (1, self.choose_class()(p)), self.model.predict_proba(data)))
