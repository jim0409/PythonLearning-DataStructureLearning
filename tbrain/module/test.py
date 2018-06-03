import pickle

with open('pickle_example.pickle', 'rb') as file:
    test_dic = pickle.load(file)

print(test_dic)
