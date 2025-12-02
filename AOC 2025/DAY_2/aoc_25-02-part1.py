from os.path import join, realpath, dirname


def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().strip()


def generate_invalid_in_range(start, end):
    invalid_ids = []
    max_len = len(str(end))

    for length in range(2, max_len + 1, 2):
        half_len = length // 2
        start_half = 10 ** (half_len - 1)
        end_half = 10 ** half_len - 1

        for n in range(start_half, end_half + 1):
            repeated = int(str(n) * 2)
            if start <= repeated <= end:
                invalid_ids.append(repeated)
            elif repeated > end:
                break
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
