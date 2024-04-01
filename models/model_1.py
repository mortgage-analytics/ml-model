from typing import Tuple
import pandas as pd
import numpy as np 

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

        # theres probably a better way without for loop
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
        return (0, 0)


    def export_model(self, file_name:str):
        """
        Exports feature means and variances in a file
        """
        pass

    def load_model(self, file_name:str):
        """
        Imports feature means and variances in a file
        """
        pass


if __name__ == "__main__":
    # df = pd.read_csv('training_data.csv')
    # target_column = ['application_stage']

    # predictors = list(set(list(df.columns))-set(target_column))     # not include those two columnjjhs

    # inputs = df[predictors].values
    # output = df[target_column].values

    # input_train, input_test, output_train, output_test = train_test_split(inputs, output, test_size = 0.2, random_state = 30)
    #

    data = np.random.randint(0, 2, (10, 7))
    model = Model(features=6, classes=2)
    model.train(data)
