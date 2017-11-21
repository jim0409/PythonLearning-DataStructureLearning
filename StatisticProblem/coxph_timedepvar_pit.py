import numpy as np
import lifelines

class dataInfo():
    def __init__(self, censor_rate=0, par_coef_time_dep=0, par_var_time_dep=0, beta=0, landa=0 ):
        self.censor_rate = censor_rate
        self.par_coef_time_dep = par_coef_time_dep
        self.par_var_time_dep = par_var_time_dep
        self.beta = beta
        self.landa = landa

def inversecdf(intercet, slope, beta, landa, data):
    simulate_data = np.log( 1 + slope * beta * np.array(data) * np.exp( -intercet * beta ) / landa )/( slope * beta)
    return simulate_data


if __name__ == '__main__':

    newData = dataInfo(censor_rate=1, par_coef_time_dep=1, par_var_time_dep=1, beta=1, landa=1)
    data = [1, 2, 3, 4, 5]

    result = inversecdf(intercet=1, slope=1, beta=newData.beta, landa=newData.landa , data=data)

    print(newData.landa)

    print(result)
