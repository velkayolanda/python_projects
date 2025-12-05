from os.path import join, dirname, realpath

def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

def parse_ranges(lines):
    ranges = []
    for line in lines:
        if line == "":
            break
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    return ranges

def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()
    merged = [ranges[0]]

    for current in ranges[1:]:
        last_start, last_end = merged[-1]
        curr_start, curr_end = current

        if curr_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, curr_end))
        else:
            merged.append(current)

    return merged

def count_all_fresh_ids(ranges):
    merged = merge_ranges(ranges)
    total = 0
    for start, end in merged:
        total += end - start + 1
    return total

def main():
    lines = read_input("input.txt")
    ranges = parse_ranges(lines)
    result = count_all_fresh_ids(ranges)
    print(result)

if __name__ == "__main__":
    main()
