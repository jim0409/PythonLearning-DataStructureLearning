import numpy as np
from sklearn import datasets
from sklearn import svm

# #use numpy to read csv is not so difficult
# test =np.genfromtxt('fileb.csv',delimiter=',') #,dtype=None)  #dtype will effect the value put in our array
#
# print(test)

#I want to use sklean database to test the function
iris = datasets.load_iris()
digits = datasets.load_digits()

# print(digits.data)
# print(type(digits.data))
# print(digits.target)
# print(digits.images[0])

clf = svm.SVC(gamma=0.001, C=100.)
print(clf.fit(digits.data[:-1], digits.target[:-1]))
print(clf.predict(digits.data[-1:]))
