from random import randint
from art import logo  # Assuming there's an 'art' module with an ASCII art logo

def game_difficulty_level(choice):
    """
    Determines the number of attempts allowed based on the chosen difficulty level.

    Parameters:
        choice (str): Difficulty level entered by the user ("easy" or "hard").

    Returns:
        int: Number of allowed guesses (10 for easy, 5 for hard).
    """
    return 10 if choice == "easy" else 5

def check_user_guess(guess, number):
    """
    Compares the user's guess to the target number and provides feedback.

    Parameters:
        guess (int): The number guessed by the user.
        number (int): The actual number to be guessed.

    Returns:
        bool: True if the guess is correct, False otherwise.
    """
    if guess > number:
        print("Too high")
        print("Guess again")
        return False
    elif guess < number:
        print("Too low")
        print("Guess again")
        return False
    else:
        print(f"Correct! You guessed right. The number was {number}")
        return True

def main():
    """
    Main function that runs the number guessing game.
    It handles difficulty selection, manages user input, and tracks remaining attempts.
    """
    print(logo)  # Display ASCII art logo
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number = randint(1, 100)

    # Prompt user to select difficulty level
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives_remaining = game_difficulty_level(difficulty_level)

    is_correct_guess = False

    # Loop until the user guesses correctly or runs out of attempts
    while lives_remaining > 0 and not is_correct_guess:
        print(f"You have {lives_remaining} attempts remaining to guess the number.")

        try:
            # Prompt user for a guess
            guess = int(input("Make a guess: "))
        except ValueError:
            # Handle non-integer input
            print("That's not a number. Try again.")
            continue

        # Check the user's guess and update game state
        is_correct_guess = check_user_guess(guess, number)
        if not is_correct_guess:
            lives_remaining -= 1  # Decrease attempts on wrong guess

    # Inform the user if they run out of attempts
    if not is_correct_guess:
        print(f"You run out of guesses! You lose. The number was {number}.")

# Run the game when the script is executed
if __name__ == "__main__":
    main()
