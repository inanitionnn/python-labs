"""X value [A,B]"""
A = 0
B = 1


def s(x: float, eps: float) -> float:
    """
	Calculate the equation

	ind - current index
	cur - current value of n member
	sum - cureent value of amountd
	"""
    ind = 0
    cur = x / 2
    sum = cur

    while cur >= eps or cur <= -eps:
        cur *= x * (ind * ind + 2 * ind + 1) / \
               (4 * ind * ind + 14 * ind + 12)
        sum += cur
        ind += 1

    return sum


def read_x():
    """
	Read and check x

	x must be [A,B]
	"""
    x = float(input("Enter the X value [0,1]: "))
    if x <= A or x >= B:
        raise ValueError("Undefined")
    else:
        return x


def read_eps():
    """
	Read and check eps

	eps must be >=0
	"""
    eps = float(input("Enter the Epc value [eps>=0]: "))
    if eps <= 0:
        raise Exception("Wrong input")
    else:
        return eps


def main():
    print("""Lab2,  Tarasiuk Oleksandr, K-13
	Variant 110
	This program calculates the result of the equation 
	from the entered X and Eps""")
    try:
        x = read_x()
        eps = read_eps()
        print("***** do calculations ... ", end=" ")
        result = s(x, eps)
        print("done")
        print(f"for x = {x:.5f}")
        print(f"for eps = {eps:.4e}")
        print(f"result = {result:.9f}")
    except KeyboardInterrupt:
        print("\nprogram aborted")
    except (ValueError, EOFError, TypeError, NameError, SystemError, Exception) as e:
        print("\n***** error")
        print(e)
    finally:
        print("\nend of program ")


main()
