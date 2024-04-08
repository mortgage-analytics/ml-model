import numpy as np
from math import floor
from xgboost import XGBClassifier

class Model:
    def __init__(self, features, test_size=0.2):
        self.features = features
        self.test_size = test_size
        self._model = XGBClassifier()

    def train(self, data:np.ndarray):
        inputs = data[:, :self.features]
        outputs = data[:, self.features]

        self._model.fit(inputs, outputs)

    def evaluate(self, data:np.ndarray) -> float:
        inputs = data[:, :self.features]
        outputs = data[:,self.features]
        predictions = [round(pred) for pred in self._model.predict(inputs)]
        count = 0
        for i in range(len(data)):
            expected = int(data[i, -1])
            guess = predictions[i]
            if expected == guess:
                count += 1
        return count / len(data)



if __name__ == "__main__":
    model = Model(5)

    dataset = np.genfromtxt('training_data.csv', delimiter=',', skip_header=1)
    np.random.shuffle(dataset)
    training_size = floor(len(dataset) * .8)

    training_data = dataset[:training_size]
    testing_data = dataset[training_size:]

    model.train(training_data)

    accuracy = model.evaluate(testing_data)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
