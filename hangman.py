import random

def play_hangman():
    # 1. Use a small list of 5 predefined words
    word_list = ["python", "variable", "keyboard", "developer", "string"]
    
    # Select a random word from the list
    secret_word = random.choice(word_list)
    
    # 2. Limit incorrect guesses to 6
    incorrect_guesses_left = 6
    guessed_letters = []
    
    print("--- Welcome to Text-Based Hangman! ---")
    print(f"You have {incorrect_guesses_left} incorrect guesses allowed.")
    
    # Main game loop
    while incorrect_guesses_left > 0:
        # Build the string to display the current progress (e.g., p _ t _ _ n)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord to guess:", display_word.strip())
        
        # Check if the player has won (no blanks left)
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly:", secret_word)
            break
            
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        if guessed_letters:
            print("Letters you've already guessed:", ", ".join(guessed_letters))
            
        # Get player input
        guess = input("Guess a single letter: ").lower()
        
        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input. Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try a different one.")
            continue
            
        # Add valid guess to our list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct or incorrect using if-else
        if guess in secret_word:
            print("✅ Good guess!")
        else:
            print("❌ Incorrect guess!")
            incorrect_guesses_left -= 1
            
    # Check for loss (loop ended because incorrect_guesses_left reached 0)
    if incorrect_guesses_left == 0:
        print("\n💀 Game Over! You've run out of guesses.")
        print("The secret word was:", secret_word)

# Run the game
if __name__ == "__main__":
    play_hangman()
