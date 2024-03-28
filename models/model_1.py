import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

import torch
import torch.utils.data
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.optim as optim

# Single=0, Joint=1
# New Home=0, Existing Home=1

class ANN(nn.Module):
    def __init__(self, input_dim = 7, output_dim = 1):
        super(ANN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 32)
        self.output_layer = nn.Linear(32,1)
        self.dropout = nn.Dropout(0.15)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.output_layer(x)

        return nn.Sigmoid()(x)

if __name__ == "__main__":
    df = pd.read_csv('training_data.csv')
    target_column = ['application_stage']

    predictors = list(set(list(df.columns))-set(target_column))     # not include those two columnjjhs

    inputs = df[predictors].values
    output = df[target_column].values

    input_train, input_test, output_train, output_test = train_test_split(X, y, test_size = 0.2, random_state = 30)
    model = ANN(input_dim=6, output_dim=1)

    X_train = torch.from_numpy(input_train)
    y_train = torch.from_numpy(output_train).view(-1,1)

    X_test = torch.from_numpy(input_test)
    y_test = torch.from_numpy(output_test).view(-1,1)

    training_data = torch.utils.data.TensorDataset(X_train,y_train)
    test_data = torch.utils.data.TensorDataset(X_test,y_test)

    train_loader = torch.utils.data.DataLoader(training_data, batch_size = 64, shuffle = True)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size = 64, shuffle = True)

    loss_fn = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, weight_decay= 1e-6, momentum = 0.8)

    epochs = 1

    #model.train() # prepare model for training

    for epoch in range(epochs):
        trainloss = 0.0
        valloss = 0.0

        correct = 0
        total = 0
        for data,target in train_loader:
            data = Variable(data).float()
            target = Variable(target).type(torch.FloatTensor)
            optimizer.zero_grad()
            output = model(data)
            predicted = (torch.round(output.data[0]))
            total += len(target)
            correct += (predicted == target).sum()

            loss = loss_fn(output, target)
            loss.backward()
            optimizer.step()
            trainloss += loss.item()*data.size(0)

            trainloss = trainloss/len(train_loader.dataset)
            accuracy = 100 * correct / float(total)
            #train_acc_list.append(accuracy)
            # trainloss_list.append(trainloss)
            print('Epoch: {} \tTraining Loss: {:.4f}\t Acc: {:.2f}%'.format(
                epoch+1,
                trainloss,
                accuracy
            ))
            epoch_list.append(epoch + 1)
    
    
# correct = 0
# total = 0
# valloss = 0
# model.eval()
#
# with torch.no_grad():
#     for data, target in test_loader:
#         data = Variable(data).float()
#         target = Variable(target).type(torch.FloatTensor)
#
#         output = model(data)
#         loss = loss_fn(output, target)
#         valloss += loss.item()*data.size(0)
#
#         predicted = (torch.round(output.data[0]))
#         total += len(target)
#         correct += (predicted == target).sum()
#
#     valloss = valloss/len(test_loader.dataset)
#     accuracy = 100 * correct/ float(total)
#     print(accuracy)
