import random

def play_round():
    choices = {'r': 'Rock 🧱', 'p': 'Paper 📄', 's': 'Scissors ✂️'}
    user = input("\nYour move: 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

    if user not in choices:
        print("❌ Invalid choice! Please try again.")
        return None

    computer = random.choice(['r', 'p', 's'])

    print(f"\n🧍 You chose: {choices[user]}")
    print(f"💻 Computer chose: {choices[computer]}")

    if user == computer:
        print("🤝 It's a tie!")
        return 'tie'
    elif is_win(user, computer):
        print("✅ You won this round! 🎉")
        return 'user'
    else:
        print("❌ You lost this round! 😢")
        return 'computer'

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def game():
    print("🎮 Welcome to Rock, Paper, Scissors Game!")
    
    while True:
        user_score = 0
        computer_score = 0
        rounds = 0

        while rounds < 3:
            result = play_round()
            if result == 'user':
                user_score += 1
            elif result == 'computer':
                computer_score += 1
            elif result == 'tie':
                pass
            else:
                continue  # invalid input, don't count round

            rounds += 1
            print(f"📊 Score => You: {user_score} | Computer: {computer_score}")

        if user_score > computer_score:
            print("\n🏆 You won the game! Great job!")
        elif computer_score > user_score:
            print("\n💻 The computer wins! Better luck next time.")
        else:
            print("\n🤝 It's a draw! Well played.")

        play_again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == '__main__':
    game()
