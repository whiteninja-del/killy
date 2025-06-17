import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

housing=fetch_california_housing()
print(housing.feature_names)
print(housing.data.shape)