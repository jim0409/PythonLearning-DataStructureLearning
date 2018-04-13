inputString = ["M", "r", " ", "J", "o", "h", "n", " ", "S", "m", "i", "t", "h"]
inputlength = len(inputString)


# string : An array of char
# length : The true length of the string
# create another empty array to store!

class Solution:
    def replaceBlank(self, string, length):
        # output_string
        output_array = []
        shift = 0
        for i in range(length):
            if string[i] == " ":
                output_array.append('%')
                output_array.append('2')
                output_array.append('0')
                shift += 2
            else:
                output_array.append(string[i])

        output_len = length + shift
        return output_array, output_len


# print(inputString)

solution = Solution()

print(solution.replaceBlank(inputString, inputlength))

#
# extralen = 0
# for i in range(inputlength):
#     if inputString[i] == " ":
#         print(i)
#         for j in range(i, inputlength):
#
#         inputString[i] = "%"
#         inputString[i + 1] = "2"
#         inputString[i + 2] = "0"
#         extralen += 2
#
# inputlength += extralen
# print(inputString)
# print(inputlength)
