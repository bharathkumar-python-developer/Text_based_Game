import random

def number_guessing_game():
    # Game settings
    min_number = 1
    max_number = 100
    max_attempts = 6
    
    # Generate a random number
    number_to_guess = random.randint(min_number, max_number)
    
    # Initialize game state
    guesses = 0
    attempts_left = max_attempts
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess a number between {min_number} and {max_number}.")
    
    while attempts_left > 0:
        try:
            user_guess = int(input("Guess a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # Validate user input
        if user_guess < min_number or user_guess > max_number:
            print(f"Please enter a number between {min_number} and {max_number}.")
            continue
        
        # Increment guesses
        guesses += 1
        attempts_left -= 1
        
        # Check user guess
        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {guesses} attempts.")
            break
        elif user_guess < number_to_guess:
            print(f"Too low! You have {attempts_left} attempts left.")
        else:
            print(f"Too high! You have {attempts_left} attempts left.")
    
    # Game over
    if attempts_left == 0:
        print(f"Game over! The number was {number_to_guess}. Better luck next time.")
    
    # Play again
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing!")

number_guessing_game()
