from tbrain.src.trainetf import train_lstm
from tbrain.src.predictetf import predict_lstm
from tbrain.module.import_tfbrain_data import read_tbrain_data

# read parameter config
BATCH_START = 0  # 定義batch開始處
TIME_STEPS = 10  # 每一層有幾個ＲＮＮ - 定義10個工作天一層
BATCH_SIZE = 35  # 定義每次batch提出的量的大小
INPUT_SIZE = 1  # 放入參數個數
OUTPUT_SIZE = 1  # 輸出參數個數
CELL_SIZE = 10  # 多少個hidden units
LEARNING_RATE = 0.006  # 學習率
TRAIN_LOOP = 96  # 迭代次數
SAVING_DIR = '/Users/jimweng/PythonLearning-DataStructureLearning/tbrain/src/save_model/'

Df = read_tbrain_data('../data/taetfp.csv')  # 50 51 52
# 使用code 50的data
trainDf = Df[(Df.code == 50)]
trainDf.index = trainDf.date

# train_lstm(TRAIN_LOOP,)
# train_lstm(trainDf, TRAIN_LOOP, SAVING_DIR, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE, LEARNING_RATE)

predict_lstm(trainDf, SAVING_DIR, TIME_STEPS, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE, LEARNING_RATE)
