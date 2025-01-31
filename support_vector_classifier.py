# -*- coding: utf-8 -*-
"""Support vector classifier.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lJ0W19_rzaEmHE9zftgBoZUFHhgNzbiV
"""



"""# **Support vector clissifier implimentation**"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import make_classification
X, y = make_classification(n_samples = 1000, n_features = 2, n_classes = 2, n_clusters_per_class = 2, n_redundant = 0)

X

pd.DataFrame(X)

pd.DataFrame(X)[0]

pd.DataFrame(X)[1]

y

sns.scatterplot(x = pd.DataFrame(X)[0], y = pd.DataFrame(X)[1], hue = y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

X_train.shape

X_test.shape

from sklearn.svm import SVC

classifier = SVC(kernel = 'linear')

classifier.fit(X_train, y_train)

classifier.coef_

y_pred = classifier.predict(X_test)

y_pred

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(classification_report(y_pred, y_test))
print(accuracy_score(y_pred, y_test))
print(confusion_matrix(y_pred, y_test))

# Hyperparameter tunning

from sklearn.model_selection import GridSearchCV
params = {'C': [0.1,0.01, 2, 3, 10, 50, 100],
          'gamma': [1, 0.1, 0.2, 0.001, 0.003],
          'kernel' : ['linear']}

grid = GridSearchCV(SVC(), param_grid = params, verbose = True)
grid

grid.fit(X_train, y_train)

grid.best_params_

grid.best_score_

y_pred = grid.predict(X_test)
y_pred

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

