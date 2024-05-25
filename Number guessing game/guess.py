import random

random_num = random.randrange(1,10)
user_guess = int(input("Guess num between 1, 10: "))

if user_guess == random_num:
    print(" ")
    print(" ")
    print(" ")
    print("you won!")
    print(" ")
    print(" ")
    print(" ")
    
else:
    print("you loose", "correct answer was:", random_num)