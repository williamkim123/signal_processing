import scipy.integrate as integrate
import scipy.special as special
import math
import numpy as np


def weighted_mean(x, weights=None):
    if weights == None:
        weights = np.ones(len(x))

    sum = np.dot(x, weights)
    return sum / len(x)

#print(weighted_mean(data['channel1'].to_numpy()))

def MAV(x):
    weights = np.ones(len(x))
    sum = np.dot(x, weights)
    return sum / len(x)


def RMS():

def VAR(x, mean):
    x1 = np.square(x - mean)
    weights = np.ones(len(x))
    sum = np.dot(x1, weights)
    return sum / len(x1)-1
#mymean = MAV(data['channel1'].to_numpy())
#VAR(data['channel1'].to_numpy(), mymean)

def SD(x, mean): #REMEMBER THIS IS SCALAR
    return math.sqrt(VAR(x, mean))


def Skewness(x, mean, SD1): #SD1 is variable for standard variation
    x1 = x - mean
    x2 = np.power(x1, 3)
    weights = np.ones(len(x))
    sum = np.dot(x2, weights)/len(x2)
    SD2 = SD1**3
    return sum/SD2

def Kurtosis(x, mean, SD1):
    x1 = x - mean
    x2 = np.power(x1, 4)
    weights = np.ones(len(x))
    sum = np.dot(x2, weights) / len(x2)
    SD2 = SD1 ** 4
    return sum / SD2

def SE(SD1, n):
    return SD1/math.sqrt(n)

def MAD(x, mean):
    x1 = np.abs(x-mean)
    weights = np.ones(len(x))
    sum = np.dot(x1, weights) / len(x1)
    return sum


def classify(x):
    A = weighted_mean(x)
    B = VAR(x)

    discrimanant = 3*A - 4 #equation of the line
    

