import time
import os

def clear_screen():
    # Clear terminal screen for Windows/Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds

    print("⏳ Countdown starting...")

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"\r⏰ Time Left: {mins:02d}:{secs:02d} 🔥"
        print(timer_display, end='')
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ Time's up! ⌛️💥")

if __name__ == "__main__":
    try:
        mins = int(input("📝 Enter minutes: "))
        secs = int(input("📝 Enter seconds: "))
        clear_screen()
        countdown_timer(mins, secs)
    except ValueError:
        print("⚠️ Please enter valid numbers for minutes and seconds.")
