from math import sqrt, log, pi, exp
import os

def log_prob(x, mean, variance):
    return -0.5 * (((x-mean)**2)/variance + log(2 * pi * variance))

def normal_prob(x, mean, variance):
    return (x-mean) / sqrt(variance)

# def gauss_prob(x, mean, variance):
#     return (1/sqrt(2 * pi) * (variance**2)) * exp(-((x-mean)**2)/(2*(variance**4)))
def gauss_prob(x, mean, stdev):
    exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
    return (1 / (sqrt(2 * pi) * stdev)) * exponent

def getenv(key, default=0): return type(default)(os.getenv(key, default))
