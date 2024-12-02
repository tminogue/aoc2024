from common import deserialize_input_file
from collections import Counter

input_file_path = "./01_input.txt"

input_list = deserialize_input_file(input_file_path)


# print(f"input_list: {input_list}")

def part1(input_list: list[str]) -> int:
    total_distance = 0

    left_list = []
    right_list = []
    for row in input_list:
        left_id, right_id = row.split("   ")
        left_list.append(int(left_id))
        right_list.append(int(right_id))

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])

    return total_distance


def part2(input_list: list[str]) -> int:
    similarity_score = 0

    left_list = []
    right_list = []
    for row in input_list:
        left_id, right_id = row.split("   ")
        left_list.append(int(left_id))
        right_list.append(int(right_id))

    right_counter = Counter(right_list)
    # print(right_counter)

    for value in left_list:
        # print(f"left_list[{i}]: {left_list[i]} right_counter[left_list[{i}]]: {right_counter[left_list[i]]}")
        similarity_score += value * right_counter[value]

    return similarity_score
