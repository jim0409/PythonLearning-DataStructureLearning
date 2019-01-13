Num1= int(input('please enter the first value: '))
Num2= int(input('please enter the first value: '))

if Num1 < Num2:
    Tmp_Num = Num1
    Num1 = Num2
    Num2 = Tmp_Num
while Num2 != 0:
    Tmp_Num = Num1 % Num2
    Num1 = Num2
    Num2 = Tmp_Num

print("The gcd of the two values are :{}".format(Num1))