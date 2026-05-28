import random

# List of words
words = ["apple", "tiger", "chair", "robot", "water"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed = [word[0]]

# Number of attempts
attempts = 6

print("Welcome to Hangman!")

# Game loop
while attempts > 0:

    display = ""

    # Show guessed letters and hide others
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player won
    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check guess
    if guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")
        print("Attempts left:", attempts)

# Game over
if attempts == 0:
    print("Game Over!")
    print("The word was:", word)
