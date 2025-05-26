import random
import string
from words import words
from hangman_visual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def play_hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    print("\n🎉 Welcome to Hangman! Guess the word before you're hanged!")
    print("🔠 All letters are UPPERCASE. You have 7 lives.\n")

    while len(word_letters) > 0 and lives > 0:
        print(lives_visual_dict[lives])
        print(f"❤️ Lives left: {lives}")
        print("🔤 Used letters:", ' '.join(sorted(used_letters)))

        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("🧩 Current word: ", ' '.join(word_display))

        user_letter = input("✏️ Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"✅ Good job! {user_letter} is in the word.\n")
            else:
                lives -= 1
                print(f"❌ Nope! {user_letter} is not in the word.\n")
        elif user_letter in used_letters:
            print("⚠️ You've already guessed that letter.\n")
        else:
            print("❌ Invalid input. Please enter a single letter.\n")

    if lives == 0:
        print(lives_visual_dict[0])
        print(f"💀 Game over! The word was: {word}")
    else:
        print(f"🎉 Congratulations! You guessed the word: {word} 🎉")


def hangman():
    while True:
        play_hangman()
        play_again = input("\n🔁 Play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing Hangman! See you next time.")
            break


if __name__ == '__main__':
    hangman()
