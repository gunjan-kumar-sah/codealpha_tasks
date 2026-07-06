import random

# List of words
words = ["python", "apple", "computer", "coding", "school"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_wrong:
    display = ""

    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player has guessed the word
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong - wrong_guesses)

# Game Over
if wrong_guesses == max_wrong:
    print("\n💀 Game Over!")
    print("The correct word was:", word)