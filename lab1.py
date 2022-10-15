import math


def f(x):
    """
    Calculate the value of the equation
    :param x: Input x value in equation
    :return: Calculation result
    """
    return math.sin(21 / 47) + 13 * math.pi + \
           67 * math.e * 8 / (x - 10) / (x + 9) - \
           15 * math.acos(x - 13) + math.log(x - 6, 9)


def check_f(x):
    """
    Check if it is possible to calculate the equation
    :param x: Input x value in equation
    :return: None if calculations are not possible or
    f(x) if computation possible
    """
    if x <= 12 or x >= 14:
        return None
    else:
        return f(x)


def main():
    print("Lab1, option 110, Tarasiuk Oleksandr, k-13")
    print("This program calculates the result of the equation from the entered X")
    try:
        x = float(input("Enter the X value: "))
        print("***** do calculations ... ", end="")
        result = check_f(x)
        print("done")
        print(f"for x = {x:.8f}")
        if result is None:
            print("result = undefined")
        else:
            print(f"result = {result:.8f}")
    except (ValueError, EOFError):
        print("wrong input")
    except KeyboardInterrupt:
        print("program aborted")
    finally:
        print("end of program execution")


main()



