from typing import Tuple, List
import pandas as pd
import numpy as np
from math import pi, log, floor

def log_prob(x, mean, variance):
    return -0.5 * (((x-mean)**2)/variance + log(2 * pi * variance))

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
        output = (0, float("-inf"))

        #TODO: there is definitly a better way to do this
        for i in range(self.classes):
            prob = log(self.probabilities[i])
            for j in range(self.features):
                prob += log_prob(data[j], self.feature_means[i][j], self.feature_variances[i][j])

            if (prob > output[0]):
                output = (i, prob)

        return output


    @staticmethod
    def export_model(file_name:str):
        """
        Exports feature means and variances in a file
        """
        pass

    @staticmethod
    def load_model(file_name:str):
        """
        Imports feature means and variances in a file
        """
        pass


if __name__ == "__main__":
    data = np.genfromtxt('training_data.csv', delimiter=',', skip_header=1)

    model = Model(features=6, classes=2)
    model.train(data)

    example = data[4]
    print(data[4])
    print(model.classify(example[:-1]))
