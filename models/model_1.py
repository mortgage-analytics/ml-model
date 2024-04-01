from typing import Tuple
import pandas as pd
import numpy as np 

class Model:
    def __init__(self, features:int, classes:int):
        self.features = features
        self.classes = classes

        self.probabilities = np.zeros((self.classes))
        self.feature_means = np.zeros((self.classes, self.features))
        self.feature_variances = np.zeros((self.classes, self.features))

    def train(self, data:np.ndarray):
        """
        Trains a naive bayes classifier
        """
        pass

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

    def eval(self, data:np.ndarray) -> Tuple[int, float]:
        """
        Gives a prediction given the data, with a probability
        """
        return (0, 0)

if __name__ == "__main__":
    df = pd.read_csv('training_data.csv')
    target_column = ['application_stage']

    predictors = list(set(list(df.columns))-set(target_column))     # not include those two columnjjhs

    inputs = df[predictors].values
    output = df[target_column].values

    # input_train, input_test, output_train, output_test = train_test_split(inputs, output, test_size = 0.2, random_state = 30)
