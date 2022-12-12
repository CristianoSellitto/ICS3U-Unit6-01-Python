#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# A program that places ten random numbers from 1 to 100 in an array and calculates the average

import random


def main():
    # Places ten random numbers in an array and calculates the average

    random_array = []

    for counter in range(0, 10):
        random_number = random.randint(1, 100)
        print("Random number #{0} is {1}".format(counter + 1, random_number))
        random_array.append(random_number)
    sum_of_all_numbers = 0
    for counter in range(0, len(random_array)):
        sum_of_all_numbers = sum_of_all_numbers + random_array[counter]
    average_of_all_numbers = sum_of_all_numbers / len(random_array)
    print(
        "\nThe average of all the random numbers is {}.".format(average_of_all_numbers)
    )

    print("\nDone.")


if __name__ == "__main__":
    main()
