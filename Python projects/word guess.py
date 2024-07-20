import random

user_name = input("What's your name?: ")
print(f"Good luck, {user_name}!")

random_words = [
    "Cat", "Dog", "Tree", "House", "River", 
    "Apple", "Car", "Book", "Chair", "Sun", 
    "Moon", "Ocean", "Bird", "Shoe", "Cloud", 
    "Music", "Coffee", "Bridge", "Candle", "Rain"
]

correct_word = random.choice(random_words)
print("You have 10 attempts to guess the word.")

attempts = 0
while attempts < 10:
    user_guess = input("Enter any word: ").capitalize()
    if user_guess== correct_word:
        print("Congratulations, you guessed the correct word!")
        print("You win a 'დამწვარი უთო!'")
        break
    else:
        print("Incorrect guess. Try again!")
        attempts += 1

if attempts == 10:
    print(f"Sorry, you've run out of attempts. The correct word was '{correct_word}'.")
