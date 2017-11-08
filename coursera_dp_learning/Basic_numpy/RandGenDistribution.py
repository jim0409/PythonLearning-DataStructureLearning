import numpy as np
import matplotlib.pyplot as plt

# purpose : use inverse cdf to get a pair data for women and men height, weight
# then use logistic reg to figure a parameter. Also, try with deep learning

# how to generate random normal would refer to np.random.normal

def checkDist(sampleVector):
    plt.hist(sampleVector,20,normed=1, facecolor='blue', alpha=0.5)
    mu = sampleVector.mean().round(2)
    std = sampleVector.std().round(2)
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of Dist: $\mu=' + str(mu) + '$, $\sigma=' + str(std) + '$')
    plt.show()
    return 0

# def scatterPlot()




# generate men height and weight with sex_term 1
menHeight = np.random.normal(175,5,100)
menWeight = np.random.normal(65,0.5,100)
# checkDist(menHeight)
# print(menHeight.mean())

# scatter plot
plt.scatter(menHeight,menWeight)
plt.show()

# generate women height and weight with sex_term 0







