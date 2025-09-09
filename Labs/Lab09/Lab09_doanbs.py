# n_estimator experiment

# |   # of n_estimators |   Trial 1    |   Trial 2    |   Trial 3    |   Trial 4    |   Trial 5    |   Trial 6    |   Trial 7    |   Trial 8    |   Trial 9    |   Trial 10   |    Average   |
# ____________________________________________________________________________________________________________________________________________________________________________________________
# |   n_estimator = 1   |    81.97%    |    75.41%    |    73.77%    |    65.57%    |    85.25%    |    68.85%    |    60.66%    |    70.49%    |    68.85%    |    73.77%    |    72.46%    |
# |   n_estimator = 2   |    78.69%    |    80.33%    |    77.05%    |    57.38%    |    62.30%    |    62.30%    |    77.05%    |    63.93%    |    73.77%    |    75.41%    |    70.82%    |
# |   n_estimator = 3   |    83.61%    |    83.61%    |    73.77%    |    72.13%    |    67.21%    |    72.13%    |    81.97%    |    75.41%    |    73.77%    |    75.41%    |    75.90%    |
# |   n_estimator = 4   |    80.33%    |    73.77%    |    78.69%    |    81.97%    |    68.85%    |    63.93%    |    72.13%    |    73.77%    |    88.52%    |    80.33%    |    76.23%    |
# |   n_estimator = 5   |    75.41%    |    88.52%    |    77.05%    |    73.77%    |    83.61%    |    70.49%    |    75.41%    |    73.77%    |    78.69%    |    77.05%    |    77.38%    |
# |   n_estimator = 6   |    85.25%    |    85.25%    |    85.25%    |    63.93%    |    75.41%    |    73.77%    |    80.33%    |    78.69%    |    77.05%    |    80.33%    |    78.53%    |
# |   n_estimator = 7   |    78.69%    |    83.61%    |    80.33%    |    73.77%    |    73.77%    |    73.77%    |    80.33%    |    70.49%    |    77.05%    |    78.69%    |    77.05%    |
# |   n_estimator = 8   |    77.05%    |    81.97%    |    81.97%    |    75.41%    |    70.49%    |    67.21%    |    75.41%    |    75.41%    |    80.33%    |    78.69%    |    76.39%    |
# |   n_estimator = 9   |    81.97%    |    88.52%    |    75.41%    |    83.61%    |    73.77%    |    68.85%    |    73.77%    |    72.13%    |    78.69%    |    80.33%    |    77.71%    |
# |   n_estimator = 10  |    77.05%    |    81.97%    |    77.05%    |    81.97%    |    78.69%    |    75.41%    |    75.41%    |    72.13%    |    78.69%    |    83.61%    |    78.20%    |


import pandas as pd
import numpy as np

# Modify this to your file system
heart_disease = pd.read_csv('heart.csv') 
X = heart_disease.drop(['target'] , axis=1) 
Y = heart_disease['target']

from sklearn.ensemble import RandomForestClassifier 
# clf = RandomForestClassifier(n_estimators=1)

from sklearn.model_selection import train_test_split
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)                                                
# clf.fit(X_train, Y_train)
# y_pred = clf.predict(X_test)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)   
for j in range(1,11,1): # Run 10 trials total
    print("")
    print(f"Trial {j}:")
    print("")
    for i in range(1,11,1): # Use 1-10 estimators for the model
        print(f"Using {i} estimators: ")
        clf = RandomForestClassifier(n_estimators=i)
        clf.fit(X_train, Y_train)
        y_pred = clf.predict(X_test)
        print(f"Accuracy on test set: {clf.score(X_test, Y_test) * 100:.2f}%")
        print("")
# print(clf.score(X_train, Y_train))
# print(clf.score(X_test, Y_test))

# My Output
# 0.987603305785124
# 0.8524590163934426