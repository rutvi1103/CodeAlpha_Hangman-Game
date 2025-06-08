import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    guesses_left = 6

    while guesses_left > 0:
        print(display_word(secret_word, guessed_letters))
        print(f"Guesses remaining: {guesses_left}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
            if "_" not in display_word(secret_word, guessed_letters):
                print(f"You win! The word was {secret_word}")
                return
        else:
            guesses_left -= 1
            print("Incorrect guess.")

    print(f"You lose! The word was {secret_word}")

if __name__ == "__main__":
    hangman()