
import random

words = ["apple", "bicycle", "elephant", "galaxy", "mountain", "shadow", "thunder", "rainbow", "journey", "puzzle", "lantern", "whisper", "volcano", "diamond", "astronaut", "jungle", "melody", "fortress", "sunrise", "tornado"]
word = random.choice(words)  # Pick a random word
guessed_word = ["_"] * len(word)  # Create blank spaces
attempts = 8  # Number of incorrect guesses allowed
guessed_letters = []  # Store guessed letters

print("Welcome to Hangman!")
print(" ".join(guessed_word))  # Display initial word with underscores


while "_" in guessed_word and attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("please enter a valid response(one single letter)")
    

    if guess in guessed_letters:
        print("You already guessed that letter.")

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
                print("Correct!")
                print(" ".join(guessed_word))
    else:
        attempts -= 1
        print(f"Incorrect. You have {attempts} guesses left.")

print(" ".join(guessed_word))

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)