from math import sqrt, log, pi
import os

def log_prob(x, mean, variance):
    return -0.5 * (((x-mean)**2)/variance + log(2 * pi * variance))

def normal_prob(x, mean, variance):
    return (x-mean) / sqrt(variance)

def getenv(key, default=0): return type(default)(os.getenv(key, default))
