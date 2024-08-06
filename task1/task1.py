import sys


def main():
    # Check that got 2 arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <num1> <num2>")
        sys.exit(1)

    # Try to convert arguments to integers
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be integers.")
        sys.exit(1)

    # init counter and compute
    i = 1
    while True:
        print(i, end="")
        i = (i + m - 2) % n + 1
        if i == 1:
            break


if __name__ == "__main__":
    main()
