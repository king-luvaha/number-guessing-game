import random
import time
from collections import defaultdict

def display_welcome():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("\nDifficulty levels:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

def get_difficulty():
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_guess():
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game(difficulty, high_scores):
    # Set attempts based on difficulty
    difficulty_settings = {1: 10, 2: 5, 3: 3}
    max_attempts = difficulty_settings[difficulty]
    difficulty_names = {1: "Easy", 2: "Medium", 3: "Hard"}
    
    print(f"\nGreat! You have selected the {difficulty_names[difficulty]} difficulty level.")
    print(f"You have {max_attempts} chances to guess the correct number.")
    print("Let's start the game!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    
    while attempts < max_attempts:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        guess = get_guess()
        
        if guess == secret_number:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)
            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {time_taken} seconds")
            
            # Update high score if this is better
            if high_scores[difficulty] == 0 or attempts < high_scores[difficulty]:
                high_scores[difficulty] = attempts
                print("🎉 New high score for this difficulty level! 🎉")
            return True
        
        if attempts < max_attempts:
            if guess < secret_number:
                print(f"Incorrect! The number is greater than {guess}.")
            else:
                print(f"Incorrect! The number is less than {guess}.")
            print(f"Remaining attempts: {remaining_attempts}")
    
    print(f"\nGame over! You've run out of attempts.")
    print(f"The correct number was {secret_number}.")
    return False

def main():
    high_scores = defaultdict(int)  # Stores best attempts for each difficulty
    
    while True:
        display_welcome()
        print("\nCurrent high scores:")
        print(f"Easy: {high_scores[1] or 'No score yet'}")
        print(f"Medium: {high_scores[2] or 'No score yet'}")
        print(f"Hard: {high_scores[3] or 'No score yet'}")
        
        difficulty = get_difficulty()
        play_game(difficulty, high_scores)
        
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ['y', 'yes']:
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()