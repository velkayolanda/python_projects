from os.path import join, realpath, dirname

def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().strip()


def is_repeated_pattern(s):
    length = len(s)
    for sub_len in range(1, length // 2 + 1):
        if length % sub_len != 0:
            continue
        sub = s[:sub_len]
        if sub * (length // sub_len) == s:
            return True
    return False


def generate_invalid_in_range(start, end):
    invalid_ids = []
    for n in range(start, end + 1):
        if is_repeated_pattern(str(n)):
            invalid_ids.append(n)
    return invalid_ids


def sum_invalid_ids(ranges_line):
    total = 0
    ranges = ranges_line.split(",")

    for r in ranges:
        r = r.strip()
        if not r or "-" not in r:
            continue
        start_str, end_str = r.split("-")
        start, end = int(start_str), int(end_str)
        invalid_ids = generate_invalid_in_range(start, end)
        total += sum(invalid_ids)

    return total


def main():
    ranges_line = read_input()
    result = sum_invalid_ids(ranges_line)
    print(result)


if __name__ == "__main__":
    main()
