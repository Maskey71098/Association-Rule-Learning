#IMPORTING THE LIBRARIES
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

#IMPORTING THE DATASET
dataset = pd.read_csv('Market_Basket_Optimisation.csv')
transactions = [] 
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

#TRAINING THE ECLAT MODEL ON THE DATASET
from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)