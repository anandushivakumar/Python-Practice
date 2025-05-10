import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.") 
difficulty = input("Choose a difficulty level: type 'easy' or 'hard': ").lower()
print("You have 10 attempts to guess the number." if difficulty == "easy" else "You have 5 attempts to guess the number.")
attempts = 10 if difficulty == "easy" else 5
guess = input("Make a guess: ")
random_number = random.randint(1, 100)
while attempts > 0:
    if int(guess) == random_number:
        print(f"Congratulations! You guessed the number {random_number} correctly.")
        break
    elif int(guess) < random_number:
        print("Too low.")
    else:
        print("Too high.")
    attempts -= 1
    if attempts > 0:
        guess = input(f"You have {attempts} attempts left. Make a guess: ")