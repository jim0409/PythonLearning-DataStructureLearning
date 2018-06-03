import warnings
import itertools
import pickle
import statsmodels.api as sm
from tbrain.module.import_tfbrain_data import read_tbrain_data

# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)

# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]


def get_analytic_maps(data_file):
    data_map = {}
    etf_aic_map = {}

    df = read_tbrain_data(data_file)

    # dump data and call train function
    for index in df.code.unique():
        # separate data with codes and analysis
        data_map[index] = df[df.code == index]

        print("start train code {}".format(index))
        aic_train_result_array = train_arima_model(index, pdq, seasonal_pdq, data_map[index])

        print("finish train code {},and would append it into aic map".format(index))
        etf_aic_map[index] = aic_train_result_array

    return data_map, etf_aic_map


def train_arima_model(codeNum, pdq, seasonal_pdq, df):
    aic_result_arry = []
    warnings.filterwarnings("ignore")

    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(df[df.code == codeNum].close.values,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)

                results = mod.fit()

                aic_result = ['code:{} ARIMA{}x{}12 - AIC:{}'.format(codeNum, param, param_seasonal, results.aic)]
                aic_result_arry.append(aic_result)
            except:
                continue

    return aic_result_arry


# return analytic map and raws data map with the input param "data_path"
analytic_map, raw_data_map = get_analytic_maps('../data/taetfp.csv')

# save maps
file = open('pickle_example.pickle', 'wb')
pickle.dump(analytic_map, file)
pickle.dump(raw_data_map, file)
file.close()
