do = {"left_day": ["left_14_day","left_30_day","left_45_day"],"sensitivity":[92.86,841552,981.97]}

print(do["left_day"][0])

##演算法目的
#1. 可以用numpy讀取csv檔案 V
#2. 可以把特定字串搜索出來並且排序

#3. 重新製作矩陣

brandA = ['A','B','C']
brandB = ['D','E','F']
brandC = ['G','H','I']
brandCaseA=['A','B','C','D','E','F','D','E','F','D','E','G','H','I','G','H','I','F','A','B','C','A','B','C','A','B','G','H','I','G','H','I','C','A','B','C']
brandCase=[['A',123,456],['D',789,101],['B',789,101],['E',789,101],['G',111,222],['C',789,101],['G',111,222],['H',789,101],['G',111,222],['I',789,101],['F',789,101],['D',789,101],['G',111,222]]

NewBrandCaseA = []
NewBrandCaseB = []
NewBrandCaseC = []

for index in range(0,len(brandCase)):
    if brandCase[index][0] in brandA:
        NewBrandCaseA.append(brandCase[index])
    if brandCase[index][0] in brandB:
        NewBrandCaseB.append(brandCase[index])
    if brandCase[index][0] in brandC:
        NewBrandCaseC.append(brandCase[index])

print(type(NewBrandCaseA),NewBrandCaseA)
print(type(NewBrandCaseB),NewBrandCaseB)
print(type(NewBrandCaseC),NewBrandCaseC)