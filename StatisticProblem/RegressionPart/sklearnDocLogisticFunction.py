# http://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic.html
print(__doc__)


# Code source: Gael Varoquaux
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

# this is our test set, it's just a straight line with some
# Gaussian noise
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(np.float)
X[X > 0] *= 4
X += .3 * np.random.normal(size=n_samples)

# 利用numpy的newaxis轉變矩陣的形狀 http://ben-do.github.io/2016/09/15/change-shape-of-matrix-by-numpy/
X = X[:, np.newaxis]

# run the classifier
# C : the inverse of regularization strength; must be a positive float.
#     Like in support vector machines, smaller value specify stronger regularization
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
clf = linear_model.LogisticRegression(C=1e5)
clf.fit(X, y)

# and plot the result
plt.figure(1, figsize=(4, 3))

# plt.clf() clears the entire current figure = clear figure
# https://codeday.me/bug/20170309/5150.html
plt.clf()
plt.scatter(X.ravel(), y, color='black', zorder=20)

# 等分數字-5~10 成300個數字 https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linspace.html
X_test = np.linspace(-5, 10, 300)


def model(x):
    return 1 / (1 + np.exp(-x))
# 將值拷貝出來給loss
loss = model(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, loss, color='red', linewidth=3)

ols = linear_model.LinearRegression()
ols.fit(X, y)
plt.plot(X_test, ols.coef_ * X_test + ols.intercept_, linewidth=1)
plt.axhline(.5, color='.5')

plt.ylabel('y')
plt.xlabel('X')
plt.xticks(range(-5, 10))
plt.yticks([0, 0.5, 1])
plt.ylim(-.25, 1.25)
plt.xlim(-4, 10)
plt.legend(('Logistic Regression Model', 'Linear Regression Model'),
           loc="lower right", fontsize='small')
plt.show()
