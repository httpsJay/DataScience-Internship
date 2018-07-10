# Self Organizing Maps

# Unsupervised Deep Learning identify patterns high dimension dataset
# one of these patterns will find the fradulant way
# segmentcorrespond to specific range of values SOM
# customers are input to new space, each neuron initialised,

# winning node, guassian neighbouring function closer to the point, input space
# output space reduces dimensions, obtain with all the winning nodes
# frauds are outliers, how to detect, mean euclidean distance between in neighborhood,
# far in neurons in self-organizing maps, inverse function input associated with winning node

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# dataset => https://archive.ics.uci.edu/ml/datasets/statlog+(australian+credit+approval)
# split the dataset from Customer ID to attribute to 14 and (yes or no been approve)
# clearly distinguish who got approved and not, in priority of fradulant customers who got approved
dataset = pd.read_csv('Credit_Card_Applications.csv')

# iloc gets indexes of observation, all the lines we use : and all the columns except 
# last so :-1 and values
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# split dataset into X & Y, not trying to do supervised learning or 0 or 1 classification
# making distinction of approved and not approved customers, train SOM we will only use
# X and there's no dependent variable 

# Feature Scaling - compulsory for deep learning becase we're starting with a high 
# dimensional dataset with lots of non-linear relationship and it will be much easier
# for our deep learning models to be trained if the features are scaled. 
# use normalization all features from 0 to 1
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))

# fit sc object to X so sc gets all info (min and max) and all info for normalization
# apply normalization to X, fit method returns normalized version of X
X = sc.fit_transform(X)

# Training the SOM
# Unsupervised Learning, we don't consider
# sigma is the radius of the different neighborhoods
# learning weight, hyperparameter decides how much weight
# higher the learning rates, faster will be convergence
# lower the learning rate, the slower it takes for SOM to build
from minisom import MiniSom
som = MiniSom(x = 10, y = 10, input_len = 15, sigma = 1.0, learning_rate = 0.5)

# randomly initialize the weight vectors to small numbers close to 0
som.random_weights_init(X)

# train som on X, matrix of features and patterns recognized
som.train_random(data = X, num_iteration = 100)

# Visualising the results
# two-dimensional grid of the winning nodes
# get M-ID Mean Inter-neruon Distances, Inside the neighborhood, radius, winning 
# higher MID, winning, outlier neuron far from the general neuron, fraud, winning nodes
# with the higher M-ID. Winning node will use different nodes

from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r', 'g']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5,
         w[1] + 0.5,
         markers[y[i]],
         markeredgecolor = colors[y[i]],
         markerfacecolor = 'None',
         markersize = 10,
         markeredgewidth = 2)
show()
