import random


answer = random.randint(1,100+1)
username = input("Hi! What is your name?: ")
trial = 7

while trial : #python에서 0이 아닌 다른 값은 True이기 때문에 그냥 trial을 입력하면 trial이 0이 되면 while 문이 깨짐
    guess = eval(input( username + ", guess the number: "))

    if guess == answer:
        print("Great, You are correct. It's ", answer)
        break
    elif guess > answer:
        print("Guess again! It's too high")
    elif guess < answer:
        print("Try again! It's too low")
    trial = trial - 1
    print("You have %4d chances" % trial)
if trial == False:
    print("Sorry you got no chances..")
