# imports
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# create dataframe
patient_data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# print(patient_data.head())

# train model
def model_train(data, arr):
    # input data
    X = data.drop(columns='DEATH_EVENT')
    # output data
    y = data['DEATH_EVENT']

    # create and fit model
    model = DecisionTreeClassifier()
    model.fit(X, y)

    return model.predict([ arr ])
