import math


numb1 = eval(input("Enter a number you want: "))
numb2 = eval(input("Enter a number you want to multiply: "))

result = 0

while numb1 >= 1:
    if numb1%2 == 0:
        print("%4d %7d  struck" % (numb1, numb2))
    else:
        print("%4d %7d  keep" % (numb1, numb2))
        result = result + numb2

    numb1 = numb1 // 2
    numb2 = numb2 * 2

print("The result is %4d" % (result))