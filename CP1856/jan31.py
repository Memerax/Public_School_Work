import random


def main():
    correct = 0
    counter = 0
    # set the function to use in the while loop. (add,sub,Mult)
    mode = menu()

    while counter < 5:
        # Print question and return value to number
        number = set_mode(mode)
        guess = int(input("Guess: "))

        # compare the two
        if guess == number:
            print("Congrats, you are correct\n")
            correct += 1
        else:
            print(f"Wrong, the correct answer is {number}\n")

        counter += 1

    # end of the loop
    print(f"Number correct out of {counter} is {correct}")


def add_two_value():
    x = random.randint(25, 75)
    y = random.randint(25, 75)
    print(f"Add {x} and {y}\n")
    sum_of_x_y = x + y
    return sum_of_x_y


def subtract_value():
    x = random.randint(25, 75)
    y = random.randint(25, 75)
    print(f"Subtract {x} and {y}\n")
    sub_of_x_y = x - y
    return sub_of_x_y


def multiply_two_values():
    x = random.randint(25, 75)
    y = random.randint(25, 75)
    print(f"Multiply {x} and {y}\n")
    mult_of_x_y = x * y
    return mult_of_x_y


def set_mode(selection):
    if selection.lower() == "a":
        return add_two_value()
    elif selection.lower() == "b":
        return subtract_value()
    elif selection.lower() == "c":
        return multiply_two_values()


def menu():
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    mode = input("Choose what you want to do: ")
    return mode


if __name__ == '__main__':
    main()
