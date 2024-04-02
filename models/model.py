from typing import Tuple, List
import numpy as np
from math import log, floor
from helpers import *

class Model:
    def __init__(self, features:int, classes:int):
        self.features = features
        self.classes = classes

        self.feature_means = np.zeros((self.classes, self.features))
        self.feature_variances = np.zeros((self.classes, self.features))

    def train(self, data:np.ndarray):
        """
        Trains a naive bayes classifier
        """

        self.classes_array,self.counts = np.unique(data[:,-1], return_counts=True)
        assert self.classes_array[-1] == self.classes-1, "Number of classes in dataset is wrong"

        self.probabilities = self.counts / len(data)

        #TODO: theres probably a better way without for loop
        for i in range(len(data)):
            index = int(data[i, -1])
            self.feature_means[index] = self.feature_means[index] + (data[i, :-1] / self.counts[index])

        for i in range(len(data)):
            index = int(data[i, -1])
            self.feature_variances[index] = self.feature_variances[index] + (data[i, :-1] - self.feature_means[index])**2

        self.feature_variances = self.feature_variances / (np.reshape(np.repeat(self.counts, self.features), newshape=(self.classes, self.features))-1)


    def classify(self, data:np.ndarray) -> Tuple[int, float]:
        """
        Gives a prediction given the data, with a probability
        """
        assert self.features == len(data), "Number of features of model does not match input data"
        output = (-1, float("-inf"))

        #TODO: there is definitly a better way to do this
        for i in range(self.classes):
            #prob = self.probabilities[i]
            prob = 1
            for j in range(self.features):
                prob *= gauss_prob(data[j], self.feature_means[i][j], self.feature_variances[i][j])

            if (prob > output[1]):
                output = (i, prob)

        return output


    def save(self, file_name:str):
        """
        Exports feature means and variances in a file
        """
        print(f"Exporting model to {file_name}")


def load(file_name:str) -> Model:
    """
       Imports feature means and variances in a file
       """
    pass

if __name__ == "__main__":
    print("Loading data...")
    data = np.genfromtxt('training_data.csv', delimiter=',', skip_header=1)
    training_size = floor(len(data) * .8)

    np.random.shuffle(data)
    training_data = data[:training_size]
    testing_data = data[training_size:]

    model = Model(features=6, classes=2)
    print("Training model...")
    model.train(training_data)

    count = 0
    vals: List[int] = [0, 0]
    actual_vals: List[int] = [0, 0]
    for i in range(len(testing_data)):
        expected = int(data[i, -1])
        actual = model.classify(testing_data[i,:-1])[0]
        vals[actual] += 1
        actual_vals[expected] += 1
        #print(actual, expected)
        if (actual == expected):
            count += 1
    accuracy = count/len(testing_data)

    print("Guesses:",vals)
    print("Actual:",actual_vals)
    print(f"Accuracy: {accuracy*100:.2f}%")

    if getenv("EXPORT") == 1:
        model.save("model_file")
