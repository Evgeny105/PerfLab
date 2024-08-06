import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <array_file>")
        return

    array_file = sys.argv[1]
    with open(array_file, "r") as file:
        points = [int(line.strip()) for line in file]

    # find median
    points.sort()
    median = points[len(points) // 2]

    # generator for count steps
    steps = (abs(value - median) for value in points)

    # sum steps
    print(sum(steps))


if __name__ == "__main__":
    main()
