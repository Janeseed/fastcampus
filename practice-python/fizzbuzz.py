import random


fizzbuzz = [ str(i)*(i%3 != 0 and i%5 != 0) + "fizz"*(i%3 == 0) + "buzz"*(i%5 == 0)  for i in range(1,100+1)]
print(fizzbuzz)
## True or False를 작성하는게 스위치 처럼 사용할 수 있음.
# 혹은 나머지는 or로 처리 할 수도 있음
# 근데 이렇게 하면 숫자가 string 처리 됨.

fizzbuzz2 = ["fizz"*(i%3 == 0) + "buzz"*(i%5 == 0) or i  for i in range(1,100+1)]
print(fizzbuzz2)