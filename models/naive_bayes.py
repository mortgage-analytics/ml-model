from typing import Tuple, List
import numpy as np
from math import log, floor
from helpers import *
import os

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
        for i in range(len(data)):
            index = int(data[i, -1])
            self.feature_means[index] = self.feature_means[index] + (data[i, :-1] / self.counts[index])

        for i in range(len(data)):
            index = int(data[i, -1])
            self.feature_variances[index] = self.feature_variances[index] + (data[i, :-1] - self.feature_means[index])**2

        self.feature_variances = self.feature_variances / (np.reshape(np.repeat(self.counts, self.features), newshape=(self.classes, self.features))-1)
        print(self.feature_means)
        

    def evaluate(self, data:np.ndarray) -> Tuple[int, float]:
        """
        Gives a prediction given the data, with a probability
        """
        output = (0, float("-inf"))
        assert self.features == len(data), "Number of features of model does not match input data"

        #TODO: there is definitly a better way to do this
        for i in range(self.classes):
            prob = self.probabilities[i]
            for j in range(self.features):
                prob *= gauss_prob(data[j], self.feature_means[i][j], sqrt(self.feature_variances[i][j]))
            #print(prob, i)
            if (prob > output[1]):
                output = (i, prob)

        return output


    def save(self, file_name:str):
        """
        Exports feature means and variances in a file
        """
        with open(file_name, 'w') as file:
            file.write(f"{self.classes},{self.features}\n")
            np.savetxt(file, self.feature_means, delimiter=',', fmt='%s')
            np.savetxt(file, self.feature_variances, delimiter=',', fmt='%s')
        print(f"Exporting model to {file_name}")

    @classmethod
    def load(cls, file_name: str):
        """
        Imports feature means and variances from a file.
        """
        with open(file_name, 'r') as file:
            next(file)
            all_values = [float(value) for line in file for value in line.split(',')]

        mid = len(all_values) // 2
        feature_means_values = all_values[:mid]
        feature_variances_values = all_values[mid:]
        feature_means = np.array(feature_means_values).reshape(2, 6)
        feature_variances = np.array(feature_variances_values).reshape(2, 6)

        return feature_means, feature_variances
    

if __name__ == "__main__":
    weights_file_name = "naive_bayes_weights"
    print("Loading data...")
    data = np.genfromtxt('training_data.csv', delimiter=',', skip_header=1)
    training_size = floor(len(data) * .8)

    np.random.shuffle(data)
    training_data = data[:training_size]
    testing_data = data[training_size:]

    model = Model(features=6, classes=2)

    if getenv("LOAD")==1:
        print("Loading model...")
        model.load(weights_file_name)
    else:
        print("Training model...")
        model.train(training_data)

    count = 0
    vals: List[int] = [0, 0]
    actual_vals: List[int] = [0, 0]
    for i in range(len(testing_data)):
        expected = int(data[i, -1])
        actual = model.evaluate(testing_data[i,:-1])[0]
        vals[actual] += 1
        actual_vals[expected] += 1
        if (actual == expected):
            count += 1
    accuracy = count/len(testing_data)

    print(f"Accuracy: {accuracy*100:.2f}%")

    if getenv("SAVE") == 1:
        model.save(weights_file_name)