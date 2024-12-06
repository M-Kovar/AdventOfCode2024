# Advent of Code 2024
# https://adventofcode.com/2024

import re

import os
# Change working directory to where this script is saved
os.chdir(os.path.dirname(__file__))

# --- End of header and initialization -----------------

def get_input(input_path):
    with open(input_path, "r") as file:
        # return file.readlines()
        return file.read()
    

def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def get_mul_commands(string, use_do_instr=False):
    if use_do_instr:
        # Regex: Match everything starting with do() and ending before don't()
        do_instructions = re.findall(r"do\(\).*?(?=don't\(\))", string)
        mul_commands = [get_mul_commands(instr) for instr in do_instructions]
        mul_commands = flatten_list(mul_commands)
    else:
        # Regex: Match mul(<x>,<y>)
        mul_commands = re.findall(r"mul\(\d{1,3},\d{1,3}\)", string)

    return mul_commands


def execute_mul_commands(mul_list):
    multiplied = []

    for mul in mul_list:
        value1, value2 = re.findall(r"\d+", mul)
        multiplied.append(int(value1) * int(value2))

    return multiplied



if __name__ == "__main__":

    input_path = "input.txt"
    instructions = get_input(input_path)

    instructions = instructions.replace("\n","")
    instructions = "do()" + instructions + "don't()"

    # Part 1:
    mul_commands_part1 = get_mul_commands(instructions)
    multiplied_part1 = execute_mul_commands(mul_commands_part1)
    print(f"Part 1: {sum(multiplied_part1)}")

    # Part 2:
    mul_commands_part2 = get_mul_commands(instructions, use_do_instr=True)
    multiplied_part2= execute_mul_commands(mul_commands_part2)
    print(f"Part 2: {sum(multiplied_part2)}")