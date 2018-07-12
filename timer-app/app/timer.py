import time
import sys


class Timer:

    def __init__(self):
        self._start_time = 0
        self._learn_time = 0

    def start_timer(self):
        self._start_time = time.time()

    def pause_timer(self):
        if not self._start_time == 0:
            self.sum()

        else:
            print("First start your timer!")

    def log(self):
        differ = 0
        if not self._start_time == 0:
            differ = int(time.time() - self._start_time)

        current = time.strftime("%H:%M:%S", time.gmtime(self._learn_time + differ))
        print("Learn time: ", current)

    def stop_timer(self):
        print("Timer stopped. Everything is clear now.")
        self._start_time = 0
        self._learn_time = 0

    def sum(self):
        self._learn_time += int(time.time() - self._start_time)
        self._start_time = 0

    def timer_dialogue(self):
        print(">", end="")
        command = input()

        if command == "start":
            print("Timer is counting time now...")
            self.start_timer()

        elif command.__eq__("pause"):
            print("zzz...")
            self.pause_timer()

        elif command.__eq__("log"):
            self.log()

        elif command.__eq__("exit"):
            print("I hope see you soon. Bye!")
            self.stop_timer()
            sys.exit()

        elif command.__eq__("--help"):
            print("Available commands:")
            print("$ start - to start timer")
            print("$ pause - to pause timer")
            print("$ log - to check time")
            print("$ exit - to close application")

        else:
            print("Command not recognized. Check `--help`")

        self.timer_dialogue()