import argparse

def parse_input(input_filepath):
    with open(input_filepath, "r") as fp:
        # print(fp.read())
        all_lines = fp.readlines()
        print(all_lines)
        return all_lines
    
def parse_part_one(all_lines: list[str]):
    list_one = []
    list_two = []
    for line in all_lines:
        a = line.replace("\n", "").split(" ")
        b = [int(i) for i in a if i]
        list_one.append(b[0])
        list_two.append(b[1])
    list_one_sorted = sorted(list_one)
    list_two_sorted = sorted(list_two)
    result = 0
    for idx, item in enumerate(list_one_sorted):
        sub_result = abs(item - list_two_sorted[idx])
        print(sub_result)
        result += sub_result
    
    print(result)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser("parser for aac-2024 day 1")
    parser.add_argument("input_filepath", help="File path of input or test data")
    args = parser.parse_args()
    all_lines = parse_input(args.input_filepath)
    result = parse_part_one(all_lines)
    exit()