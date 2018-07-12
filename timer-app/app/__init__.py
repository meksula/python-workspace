from timer import Timer

timer = Timer()


def main():
    welcome()
    timer.timer_dialogue()


def welcome():
    print("Hello there!")
    print("It's time to start learning. Type '--help' if you want know more.")


if __name__ == '__main__':
    main()
