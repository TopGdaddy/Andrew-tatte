import random

word_bank = {
    "Bronze": {
        "word": "KEY",
        "hints": [
            "It is a noun.",
            "You use it to open locks.",
            "It's made of metal."
        ]
    },
    "Silver": {
        "word": "PLANET",
        "hints": [
            "The word has 6 letters.",
            "It is a noun.",
            "It orbits a star.",
            "Our home, Earth, is one."
        ]
    },
    "Gold": {
        "word": "PYTHON",
        "hints": [
            "This word is a noun.",
            "It can be a type of snake.",
            "It is also a popular programming language.",
            "Its name starts with the letter P."
        ]
    }
}

def play_door(door_name, secret_word, hints):
    print(f"\n--- Unlocking the {door_name} Door ---")
    print(f"The password has {len(secret_word)} letters.")

    chances_left = 5
    correctly_guessed_letters = ["_"] * len(secret_word)
    
    while chances_left > 0:
        print(f"\nChances remaining: {chances_left}")
        print("Password display: " + " ".join(correctly_guessed_letters))
        
        guess = input("Enter your guess: ").upper()

        if len(guess) != len(secret_word):
            print(f"Your guess must be {len(secret_word)} letters long. Try again.")
            continue

        if guess == secret_word:
            print(f"\nCorrect! The password was {secret_word}.")
            print(f"The {door_name} Door is unlocked! 🔑")
            return True

        else:
            chances_left -= 1
            print(f"Incorrect guess.")

            for i in range(len(secret_word)):
                if guess[i] == secret_word[i]:
                    correctly_guessed_letters[i] = secret_word[i]

            if chances_left > 0:
                hint_index = 4 - chances_left 
                if hint_index < len(hints):
                    print(f"Hint: {hints[hint_index]}")

    print(f"\nOut of chances! The password was {secret_word}.")
    return False

def start_game():
    print("🏆 Welcome to the 5-Door Locker Challenge! 🏆")
    print("Unlock all doors in sequence to win.")

    doors = ["Bronze", "Silver", "Gold"]

    for door in doors:
        word_data = word_bank[door]
        secret_word = word_data["word"]
        hints = word_data["hints"]
        
        if not play_door(door, secret_word, hints):
            print("\n--- GAME OVER ---")
            return
    
    print("\n🎉 CONGRATULATIONS! You have unlocked all the doors! 🎉")

if __name__ == "__main__":
    start_game()
