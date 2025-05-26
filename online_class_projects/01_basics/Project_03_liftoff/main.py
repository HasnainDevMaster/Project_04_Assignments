import time

def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)  # 1-second delay between numbers

    print("Liftoff! 🚀")

# Call the main function
if __name__ == '__main__':
    main()
