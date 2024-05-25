import random
lst = [str(i) for i in input("Enter elemets: ").split()]
print(random.choice(lst))

ext = input("type 'exit': ")
if ext == "exit":
    exit