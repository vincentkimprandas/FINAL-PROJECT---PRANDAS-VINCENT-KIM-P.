import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        # Get the user's guess
        guess = input("Enter your guess: ")

        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        # Convert the input to an integer
        guess = int(guess)
        attempts += 1

        # Check if the guess is correct
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

# Run the game
number_guessing_game()