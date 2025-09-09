## Lab 11: Regression Lab ##

_author_ = "Burgess Doan III"
_credits_ = [""]
_email_ = "doanbs@mail.uc.edu"

# Formatted with Black Formatter
# https://pypi.org/project/black/

# Script to Visualize the the Expected vs.
# Predicted Prices using Multiple Linear
# Regression Housing Price Estimator

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from matplotlib import pyplot as plt
import seaborn as sns
cali = fetch_california_housing()
cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)
cali_df['MedHouseValue'] = pd.Series(cali.target)

r2_scores = []
mse_scores = []

for feature in cali.feature_names:
    X = cali_df[[feature]]
    y = cali.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11)

    mu_regress = LinearRegression()
    mu_regress.fit(X=X_train, y=y_train)
    predicted = mu_regress.predict(X_test)
    expected = y_test
    z = zip(predicted[::1000], expected[::1000])
    r2 = r2_score(expected, predicted)
    mse = mean_squared_error(expected, predicted)
    r2_scores.append(r2)
    mse_scores.append(mse)
    # for p, e in z:
    #     print("Feature: " + feature)
    #     print(f'predicted: {p:.2f}, expected: {e:.2f}')

linear_results_df = pd.DataFrame({'Feature': cali.feature_names, 'R2 Score': r2_scores, 'MSE': mse_scores})
X_train, X_test, y_train, y_test = train_test_split(cali.data, cali.target, random_state=11)
mu_regress.fit(X=X_train, y=y_train)
predicted = mu_regress.predict(X_test)
expected = y_test
r2 = r2_score(expected, predicted)
mse = mean_squared_error(expected, predicted)
print("Multiple Linear Regression using all features:")
print("R2 score: " + str(r2))
print("MSE score: " + str(mse))
print("")
print(linear_results_df)

df = pd.DataFrame()
df['Expected'] = pd.Series(expected)
df['Predicted'] = pd.Series(predicted)


figure = plt.figure(figsize=(9, 9))
axes = sns.scatterplot(data=df, x='Expected', y='Predicted')
start = min(expected.min(), predicted.min())
end = max(expected.max(), predicted.max())
axes.set_xlim(start, end)
axes.set_ylim(start, end)
line = plt.plot([start, end], [start, end], 'k--')


# OUTPUT

# Multiple Linear Regression using all features:
# R2 score: 0.6008983115964333
# MSE score: 0.5350149774449119

#       Feature  R2 Score       MSE
# 0      MedInc  0.463081  0.719766
# 1    HouseAge  0.013186  1.322872
# 2    AveRooms  0.024105  1.308234
# 3   AveBedrms -0.001127  1.342058
# 4  Population  0.000085  1.340434
# 5    AveOccup -0.000183  1.340794
# 6    Latitude  0.020369  1.313243
# 7   Longitude  0.001484  1.338559

# SUMMARY

# Based on the R2 results, we can conclude that 
# MedInc is the only Feature that indicates some success with predicting the dependent variable's value.
# AveBedrms and AveOccup have negative R2s, and as such fit the model horribly.

# Based on the MSE results, we can conclude that
# MedInc is the only feature with somewhat accurate predictions, as it is the only MSE lower less than 1.

# Based on the results of the Multiple Regression data, we can conclude that
# Using multiple Linear Regression allows for much more accurate predictions,
# as the R2 Score is greater than any of the Single Linear Regression R2 Scores,
# and the MSE Score is less than any of the Single Linear Regression MSE Scores.