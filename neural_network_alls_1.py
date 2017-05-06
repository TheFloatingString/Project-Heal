"""
This is a sample neural network built with Keras using Tensorflow as a backend

Code is written in Python 3

This neural network goes through a dataset on cervical cancer patients

Written by: Laurence

Source for dataset:
http://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29#

"""

# IMPORT MODUELS

import csv              # Used to read CSV files

import keras            # Used for neural network
from keras.models import Sequential
from keras.layers import Dense

import numpy as np      # Used to analyze data and arrays

# DECLARE VARIABLES

master_array = []       # Stores all the raw data
master_array_2 = []     # Stores all the treated data

X = []                  # Untreated data
Y = []                  # Results

# Description of the program
print("THIS IS A SAMPLE NEURAL NETWORK USED ON PATIENT DATA FOR CERVICAL CANCER")


# Define functions

# Read CSV file function
def read_file(file_name):

    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')  # Delimits

        for row in readCSV:
            master_array.append(row)    # Appends to master_array

# Remove rows with '?' function
def remove_symbol(symbol, array_pr, new_array):
    for row in array_pr:
        if symbol in row:
            array_pr.remove(row)    # Removes rows with list
        else:
            new_array.append(row)

# Process array function
def process_array(array_pr):
    for row in array_pr:        # For each row
        array_pr = [ float(item) for item in row ]

def list_size_2dim(array_pr):
    print(len(array_pr))

# Load dataset
read_file('risk_factors_cervical_cancer.csv')
print("Reading file...")

# Remove symbol
remove_symbol('?', master_array, master_array_2)
print("Processing data")

# Process array
del master_array_2[:2]    # Removes first 2 rows

process_array(master_array_2)
print("Converting data")

print("Number of items:")
print(len(master_array_2))

# Assign data to lists

# Y: Results
for row in master_array_2:
    row = [float(x) for x in row]
    Y.append(row[26])
    print(row[26])
    X.append(row)

# X: Data


print("Data ready \n")


# Build neural network
# Sequential
model = Sequential()

# Neural network
model.add(Dense(36, input_dim=34, init='uniform', activation='sigmoid' ))
model.add(Dense(32, init='uniform', activation='sigmoid'))
model.add(Dense(32, init='uniform', activation='sigmoid'))
model.add(Dense(32, init='uniform', activation='sigmoid'))
model.add(Dense(33, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='mean_squared_logarithmic_error', optimizer='SGD', metrics=['accuracy'])

# Fit model
history = model.fit(X, Y, nb_epoch=20, validation_split=0.2, batch_size=3)

# Analysis
