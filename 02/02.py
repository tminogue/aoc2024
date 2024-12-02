from common import deserialize_input_file


input_list = deserialize_input_file("./02_input.txt")
input_reports = []
for report in input_list:
    levels = [int(level) for level in report.split(" ")]
    input_reports.append(levels)



def is_safe_report(report) -> bool:
    # print(f"    report passed to is_safe_report: {report}")
    for idx, level in enumerate(report):
        # print(f"    idx: {idx} level: {level}")

        if idx == len(report) - 1:
            # return True if we have reached the last level in the list
            return True

        is_report_level_increasing = report[1] > report[0]

        diff = abs(report[idx+1] - report[idx])
        is_diff_increasing = report[idx+1] > report[idx]

        if  any(
                [
                    diff > 3,
                    diff == 0,
                    is_diff_increasing != is_report_level_increasing
                ]
        ):
            return False

    return True



def part1(input_reports):
    safe_report_count = 0

    for report in input_reports:
        # print("report: ", report)
        if is_safe_report(report):
            safe_report_count += 1

    return safe_report_count


def part2(input_reports) -> int:
    # First test the report list to see if it is safe without removing any levels
    # If it is safe, increment the safe_report_count
    # If it is not safe, test removing each level in the report list to see if it becomes safe
    #   If it becomes safe, increment the safe_report_count
    #   Otherwise, move on to the next level in the list and test if it is safe

    safe_report_count = 0

    for report in input_reports:
        is_safe = is_safe_report(report)

        if is_safe:
            safe_report_count += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                is_safe = is_safe_report(modified_report)
                if is_safe:
                    safe_report_count += 1
                    break

    return safe_report_count
