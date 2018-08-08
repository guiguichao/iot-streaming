import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.externals import joblib
import time
#import seaborn as sns

#load raw datasets

print("Loading in sample data====================")
df = pd.read_csv('sample_data.csv')
print(df)
#print(data[['Reading 1']].shape)

#sns.pairplot(df, x_vars=['s1', 's2', 's3'], y_vars='target', size=7, aspect=0.7, kind='reg')
# create a Python list of feature names
feature_cols = ['s1', 's2', 's3', 's4']
# use the list to select a subset of the original DataFrame
X = df[feature_cols]
y = df['target']

print("Splitting sample data into training and testing data====================")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

print("X traing dataset size: " )
print(X_train.shape)
print("X testing dataset size: " )
print(X_test.shape)
print("y traing dataset size: " )
print(y_train.shape)
print("y testing dataset size: " )
print(y_test.shape)

#data normailization
#df['split'] = np.random.randn(df.shape[0], 1)
#split = np.random.rand(len(df)) <= 0.75
#print(split)

#X_train = df[split]
#print(X_train)
#X_test  = df[~split]
#training_data = np.array(data['Reading 1'], data['Reading 2'])

#print(training_data(1).shape)

# Create linear regression object
linreg = linear_model.LinearRegression()

print("Training the model====================")
# Train the model using the training sets
linreg.fit(X_train, y_train)

# print the intercept and coefficients
print(linreg.intercept_)
print(linreg.coef_)

print("Saving the model====================")
joblib.dump(linreg, 'linreg.pkl')
print("Model saved====================")

time.sleep(2)
print("Loading the model====================")
clf = joblib.load('linreg.pkl')
y_pred = clf.predict(X_test)
print(y_pred)

# make predictions on the testing set
#y_pred = linreg.predict(X_test)
