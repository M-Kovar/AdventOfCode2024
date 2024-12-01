# Advent of Code 2024
# https://adventofcode.com/2024/day/01

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------


def get_input(input_path):
    list_left = []
    list_right = []
    with open(input_path, "r") as file:
        for line in file:
            left, right = line.split("   ")
            list_left.append(int(left.strip()))
            list_right.append(int(right.strip()))
    return list_left, list_right


if __name__ == "__main__":

    input_path = "input.txt"
    list_left, list_right = get_input(input_path)

    # Part 1:
    list_left_sorted = sorted(list_left)
    list_right_sorted = sorted(list_right)
    list_part1 = [abs(left - right) for left, right in zip(list_left_sorted, list_right_sorted)]

    print(f"Part 1: {sum(list_part1)}")
    
    # Part 2:
    list_part2 = [id * list_right.count(id) for id in list_left]

    print(f"Part 2: {sum(list_part2)}")