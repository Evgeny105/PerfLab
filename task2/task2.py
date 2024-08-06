import sys
import math


def read_circle_data(file_path):
    with open(file_path, "r") as file:
        center = tuple(map(float, file.readline().strip().split()))
        radius = float(file.readline().strip())
    return center, radius


def read_points_data(file_path):
    with open(file_path, "r") as file:
        points = [tuple(map(float, line.strip().split())) for line in file]
    return points


def is_point_inside_circle(center, radius, point):
    distance = math.sqrt(
        (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2
    )
    if math.isclose(distance, radius, abs_tol=1e-9):
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    center, radius = read_circle_data(circle_file)
    points = read_points_data(points_file)

    for point in points:
        print(is_point_inside_circle(center, radius, point))


if __name__ == "__main__":
    main()
