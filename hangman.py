import random

# List of predefined words
words = ["apple", "tiger", "house", "plant", "chair"]

# Randomly choose a word
chosen_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while attempts > 0:

    # Display the word with blanks
    display_word = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word!")
        break

    # User input
    guess = input("Guess a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Correct guess
    if guess in chosen_word:
        print("✅ Correct guess!")

    # Wrong guess
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)

# If user loses
if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", chosen_word)