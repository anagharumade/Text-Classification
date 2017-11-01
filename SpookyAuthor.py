# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 07:25:19 2017

@author: absol
"""
import os
os.chdir('E:\Miscellaneous\Kaggle\SpookyAuthor')

import pandas as pd

data = pd.read_csv('train.csv')
X = data.iloc[:, 1].values
Y = data.iloc[:, 2].values

#import google.datalab.bigquery as bq
data['author'].value_counts()

#Splitting into train and test data
from sklearn.cross_validation import train_test_split
train_X, train_Y, test_X, test_Y = train_test_split(X, Y, test_size = 0.2)

