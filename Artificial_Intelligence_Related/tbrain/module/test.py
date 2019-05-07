import pickle
import csv

with open('pickle_example.pickle', 'rb') as file:
    test_dic = pickle.load(file)

with open('some.csv','w',newline='') as f:
    for i in test_dic.keys():
        writer = csv.writer(f)
        writer.writerows(test_dic[i])
