#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Oct 10, 2023
# This program make you guess between 1 to 9

import constants


def main():
    user_guess = int(input("Your guess is: "))
    print("")

    if user_guess == constants.CORRECT_GUESS:
        # check if he guessed correctly
        print("You guess correctly.")
    if user_guess != constants.CORRECT_GUESS:
        # check if he guessed correctly
        print("You guess incorrectly")


if __name__ == "__main__":
    main()
