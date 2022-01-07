#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Dec 2021
# Largest Number


def main():
    # main function for creating largest number program

    try:
        # input
        num1 = input("First Number: ")
        num1 = int(num1)
        num2 = input("Second Number: ")
        num2 = int(num2)
        num3 = input("Third Number: ")
        num3 = int(num3)

        # process
        if (num1 >= num2) and (num1 >= num3):
            largest = num1
        elif (num2 >= num1) and (num2 >= num3):
            largest = num2
        else:
            largest = num3
        
        # output
        print(f"Largest Number is {largest}.")
    except ValueError:
        print("Input must be an integer")
    finally:
        # done
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
