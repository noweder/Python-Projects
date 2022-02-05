from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
# remaining_attempts = attempts
# print(f"You have {remaining_attempts} attempts remaining to guess the number.")

number = random.randint(1, 100)
game_over = False
while game_over == False:
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {guess}.")
            game_over = True
        else:
            attempts -= 1
            if guess > number:
                print("Too high.")
            elif guess < number:
                print("Too low.")
            if attempts != 0:
                print("Guess again.")

    else:
        game_over = True
        print("You've run out of guesses, you lose.")