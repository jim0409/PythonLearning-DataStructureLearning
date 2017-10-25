import pandas as pd
import numpy as np
import datetime
from sklearn.externals import joblib

#This function will split input names  with '/' also
#given first parameter with filename, second parameter with position, and third parameter with separate symbol
def namePosSepS(filename,pos,sepS):
    inputName = filename
    return inputName.split(sepS)[pos]

#This fucntion wiil classify data with specify index (note: length of specify index must be as the same as the data rownumbers)
#given first paramter with datafile, criterion column, and specifyIndex
def specifyData(datafile, critCol, speIndex):
    tempData=pd.DataFrame(columns=datafile.columns.values)
    for index in range(0,len(critCol)):
        if speIndex in critCol[index]:
            tempData=tempData.append(datafile.values.tolist()[index],ignore_index=True)
    return tempData

def predictData(datafile,proj,brand):
    resultColname = ["date", "serial_number", "model", "remaining_day", "early_warning", "sensitivity","average_waste_day", "predict_model", "attribute_used"]
    resultData = pd.DataFrame(columns=resultColname)
    return 0

if __name__ == '__main__':
    # define database
    # df = pd.read_table('url',sep=',')
    # predictData=pd.read_table("data.csv",sep=",")
    a=namePosSepS(filename="1212313/1456", pos=0, sepS='/')
    print(a)

    # testdata=specifyData(datafile=df, critCol=df.E, speIndex='train')
    # print(testdata)
