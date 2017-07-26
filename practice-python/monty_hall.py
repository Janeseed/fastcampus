# 몬티홀 문제 풀기
import random


stay = 0
switch = 0 # 변수 선언 및 initiallizing

for i in range(1000): # 이렇게 하면 0부터 999까지
    doors = [1,0,0]
    random.shuffle(doors)

    choice = random.randrange(3)
    user = doors[choice] #index를 이런식으로도 쓸 수 있음. choice번 자리에 있는 list의 요소

    if user == 1:
        stay = stay + 1
    else:
        switch = switch + 1

print("The car showed %6d times in the door" % (stay))
print("The goat showed %5d times in the door" % (switch))