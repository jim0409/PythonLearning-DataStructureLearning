# 筆記：一開始以為只是單純比較字符，後來發現題目用意是要比較兩邊字串內的元素均要一致！所以需要考驢到存在/存在個數於是決定用dictionary來做～
a = 'abbe'
# b = 'abe'
b = 'aebb'

# since the original declaration of python is list,
# no need to separate or claim an array to store it
# check string length
# check exists
# check each elements length

# create a map to store element and cout it!
# use one of its key to map and check whether they exists or not

# class Solution:
#     def Permutations(self, A, B):
#         if len(A) != len(B):
#             return False
#         for i in A:
#             if self.check_exist(i,B):
#                 pass
#             else:
#                 return self.check_exist(i,B)
#         for j in B:
#             if self.check_exist(j,A):
#                 pass
#             else:
#                 return self.check_exist(j,A)
#         return True
#
#     def check_exist(self,stringA, stringB):
#         for j in stringB:
#             if stringA == j:
#                 return True
#         return False
#
# def MapReturn(A):
#     map_A = {}
#     for i in A:
#         if i in map_A.keys():
#             # print("enter here")
#             map_A[i] = map_A[i] + 1
#         else:
#             map_A[i] = 1
#     return map_A


class Solution:
    def Permutations(self, A, B):
        mapA = self.map_return(A)
        mapB = self.map_return(B)
        return (mapA == mapB)

    def map_return(self,A):
        map_A = {}
        for i in A:
            if i in map_A.keys():
                # print("enter here")
                map_A[i] = map_A[i] + 1
            else:
                map_A[i] = 1
        return map_A



c = Solution()
print(c.Permutations(A=a, B=b))
