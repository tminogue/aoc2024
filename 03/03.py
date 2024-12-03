import re

from common import deserialize_input_file

input_list = deserialize_input_file("./03_input.txt")


test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
test_list = [test_string]

valid_mul_pattern = r"mul\(\d+,\d+\)"


def part1(input_list) -> int:
    total_product = 0

    for row in input_list:
        row_product = 0
        matches = re.findall(valid_mul_pattern, row)

        for match in matches:
            stripped = match.replace("mul(", "").replace(")", "")
            val_string_1, val_string_2 = stripped.split(",")
            val_1 = int(val_string_1)
            val_2 = int(val_string_2)
            row_product += val_1 * val_2

        total_product += row_product

    return total_product


def part2(input_list) -> int:

    # concatenate the all the strings in the list to a single string
    input_string = "".join(input_list)

    start_pattern = r"do\(\)"
    stop_pattern = r"don\'t\(\)"

    # build a list of strings that between the start and stop indexes
    # these strings will be passed to part1 for processing
    valid_do_strings = []

    # search the string for the next stop pattern, if not found, return the string
    # if found, slice the string from the start index to the stop index
    # then search the new string for the next start and stop indexes
    # repeat until no more stop indexes are found

    # Find the first stop index in the string
    stop_match = re.search(stop_pattern, input_string)


    while stop_match:
        # add the substring between start of string and stop index to the valid_do_strings list
        valid_do_strings.append(input_string[:stop_match.start()])
        # truncate the input string to the substring after the stop index
        input_string = input_string[stop_match.end():]

        # search for new start pattern in the newly truncated string
        start_match = re.search(start_pattern, input_string)
        # if there is no start pattern, exit the loop
        # if there is a start pattern, truncate the string to the substring after the start index

        if start_match:
            input_string = input_string[start_match.end():]
        else:
            break

        stop_match = re.search(stop_pattern, input_string)


    # for i, string in enumerate(valid_do_strings):
    #     print(f"{i}:  {string}")

    return part1(valid_do_strings)

