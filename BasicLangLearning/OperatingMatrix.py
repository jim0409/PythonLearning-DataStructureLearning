import copy
class selfDefineMatrix:
    def __init__(self,r=0,c=0):
        self.dimR=r
        self.dimC=c
    def printDim(self):
        return print("the row's : ", self.dimR ,"the col's : ", self.dimC)
    def buildMatrix(self):
        matrixOperator= []
        for i in range(0, self.dimR):
            new = []
            for j in range(0, self.dimC):
                new.append(input(">>"))
            matrixOperator.append(new)
        return matrixOperator

#write a row operation  r2 = r1*c + r2
def rowOperation(rMatrix,r1,r2,c):
    for index in range(0,len(rMatrix[0])):
        rMatrix[r2][index] = rMatrix[r2][index] + c*rMatrix[r1][index]
    return rMatrix

#write a col operation
def colOperation(cMatrix,c1,c2,c):
    for index in range(0,len(cMatrix)):
        cMatrix[index][c2] = cMatrix[index][c2] + c*cMatrix[index][c1]
    return cMatrix

# def productMatrix(m1,m2):
def multiMatrix(matrix1,matrix2):
    multimatrix = []
    for indexI in range(0, len(matrix1)):
        new=[]
        for indexJ in range(0, len(matrix2)):
            tmp=0
            for indexK in range(0, len(matrix1[0])):
                tmp = tmp + matrix1[indexI][indexK]*matrix2[indexK][indexJ]
            new.append(tmp)
        multimatrix.append(new)
    return multimatrix

#define Gaussian Inverse Matrix
# def gaussianInverse(rMatrix):


if __name__ == '__main__':

    identyMatrix=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # print(id(identyMatrix)) #address

    testMatrix = list()
    for i in range(len(identyMatrix)):
        testMatrix.append(copy.copy(identyMatrix[i]))
    # print(id(testMatrix)) #address

    print(rowOperation(rMatrix=testMatrix,r1=0,r2=1,c=1))
    print(multiMatrix(testMatrix,testMatrix))

    print(identyMatrix)
