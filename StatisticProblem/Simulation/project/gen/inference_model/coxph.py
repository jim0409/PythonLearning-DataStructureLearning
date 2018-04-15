# step 1. build a rexp to simulate life
# step 2. formula in statistical model to transform it to particular life model
# step 3. recheck model fit with cox model

# step 4. create time dependent covariates variable for its' particular life
# step 5. separate it as statistical method
# step 6. notice with some statistical theory as refer

import numpy as np
import matplotlib.pyplot as plt
import lifelines


# will need sample_size to know how many simulation data needed
# censor_rate to make sure not too much data censor
# intercept means the base risk of each vairable
# slop terms for the increasing rate of risk
# beta and landa is the same define as coxph
# cov_type(time dep) default is linear
class dataInfo():
    def __init__(self, sample_size, censor_rate=0, intercept=0, slope=0, beta=0, landa=0, cov_type="linear"):
        self.sample_size = sample_size
        self.censor_rate = censor_rate
        self.intercept = intercept
        self.slope = slope
        self.beta = beta
        self.landa = landa

    def genTimeData(self):
        surv_T = np.random.exponential(scale=self.landa, size=self.sample_size)
        return surv_T

    def genEventData(self):
        event_T = np.random.exponential(scale=self.landa, size=self.sample_size)
        return event_T


def inversecdf(intercet, slope, beta, landa, data, cov_type="linear", error_term=False):
    simulate_data = np.log(1 + slope * beta * np.array(data) * np.exp(-intercet * beta) / landa) / (slope * beta)
    return simulate_data


if __name__ == '__main__':
    newData = dataInfo(sample_size=1000, censor_rate=1, intercept=1, slope=1, beta=1, landa=1)
    data = [1, 2, 3, 4, 5]

    result = inversecdf(intercet=newData.intercept, slope=newData.slope, beta=newData.beta, landa=newData.landa,
                        data=data)

    plt.hist(newData.genTimeData(), normed=1, facecolor="green", alpha=0.5)
    plt.show()
