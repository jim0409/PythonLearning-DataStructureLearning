# OrederedDict 主要是用來排序字母
from collections import OrderedDict
# 使用python DB
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# 視覺化資料
import seaborn as sns
# 存活分析用套件
import lifelines as sa
from lifelines.utils import concordance_index, k_fold_cross_validation
import patsy as pt
# suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Set default styles for plotting via pandas, seaborn and matplotlib
pd.set_option('display.mpl_style', 'default')
pd.set_option('display.notebook_repr_html', True)
sns.set(style='darkgrid')
cmap_clrbld = ['#777777','#E69F00','#56B4E9','#D3C511'
               ,'#009E73','#8D42F0','#0072B2','#D55E00','#CC79A7']
plt.rcParams['axes.color_cycle'] = cmap_clrbld
plt.rcParams['figure.figsize'] = 10, 6

np.random.seed(0)

def estimate_cond_mean(S):
    """ Quick & dirty estimate of conditional mean lifetime """
    fstar = -S.diff() / (1 - S.iloc[-1, 0])
    Sstar = (S - S.iloc[-1, 0]) / (1 - S.iloc[-1, 0])
    llstar = fstar / Sstar

    llstar[pd.isnull(llstar)] = 0
    llstar = llstar[np.isfinite(llstar)]
    llstarcs = llstar.cumsum().reset_index()
    llstarcs['timelinediff'] = np.append(llstarcs['timeline'].diff().values[1:], 0)
    llstarcs['auc'] = llstarcs['timelinediff'] * llstarcs['KM_estimate']
    return np.nansum(llstarcs['auc']).round()

cnx = sqlite3.connect('data/drive_stats.db')
df = pd.read_sql('select * from drive_survival_prepared', con=cnx
                 ,index_col='diskid', parse_dates=['mindate','maxdate'])

# print(df.shape)
# df.head()

modelspec = 'manufacturer + capacity'

dft = pt.dmatrix(modelspec, df, return_type='dataframe')
design_info = dft.design_info
dft = dft.join(df[['maxhours','failed']])

## NOTE: CoxPHFitter expects reduced-rank design matrix WITHOUT intercept
## https://courses.nus.edu.sg/course/stacar/internet/st3242/handouts/notes3.pdf
del dft['Intercept']
dft.head().T

cx = sa.CoxPHFitter(normalize=False)
cx.fit(df=dft, duration_col='maxhours', event_col='failed'
           ,show_progress=True, include_likelihood=True)

fig, axes = plt.subplots(nrows=1, ncols=2, squeeze=False, sharex=True)
cx.baseline_cumulative_hazard_.plot(ax=axes[0,0], legend=False
                ,title='Baseline cumulative hazard rate')
cx.baseline_survival_.plot(ax=axes[0,1], legend=False
                ,title='Baseline survival rate')

cx.summary

smy = cx.summary.copy().reset_index()
smy['type'] = smy['index'].apply(lambda x: 'mfr' if x[:1]=='m' else 'cap')
smy['err'] = smy['upper 0.95'] - smy['coef']

fig, axes = plt.subplots(nrows=1, ncols=2, squeeze=False, figsize=(10,6), sharey=True)
fig.canvas.draw()
for j, sel in enumerate(['mfr','cap']):
    smysub = smy.loc[smy['type']==sel].copy()
    axes[0,j].errorbar(x=np.arange(smysub.shape[0]), y=np.exp(smysub['coef'])
                       ,marker='o', linestyle='', yerr=np.exp(smysub['err']))
    axes[0,j].set_title('exp(beta) coefs for {}'.format(['manufacturer','capacity'][j]))
    axes[0,j].set_xlim([-0.1, len(smysub) - 0.9])
    axes[0,j].set_xticks(np.arange(smysub.shape[0]))
    axes[0,j].set_xticklabels([t.split('[')[1][2:-1] for t in smysub['index']])

cx1 = sa.CoxPHFitter(normalize=False)
scores = k_fold_cross_validation(cx1, dft, k=5
        ,duration_col='maxhours',event_col='failed', predictor='predict_expectation')

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10,2))
sns.boxplot(scores, vert=False, color='lightblue', ax=axes, showmeans=True)
axes.annotate('{:.3f}'.format(np.mean(scores)), xy=(np.mean(scores),1), xycoords='data'
                 ,xytext=(10, 10), textcoords='offset points', color='r', fontsize=12)
axes.set_xlim([0.5,1])