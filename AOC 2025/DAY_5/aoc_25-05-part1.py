from os.path import join, dirname, realpath

def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

def parse_input(lines):
    try:
        sep_index = lines.index("")
    except ValueError:
        sep_index = len(lines)

    range_lines = lines[:sep_index]
    id_lines = lines[sep_index + 1:]

    ranges = []
    for line in range_lines:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ingredient_ids = list(map(int, id_lines))

    return ranges, ingredient_ids

def is_fresh(ingredient_id, ranges):
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def count_fresh_ingredients(ranges, ingredient_ids):
    count = 0
    for iid in ingredient_ids:
        if is_fresh(iid, ranges):
            count += 1
    return count

def main():
    lines = read_input("input.txt")
    ranges, ingredient_ids = parse_input(lines)
    result = count_fresh_ingredients(ranges, ingredient_ids)
    print(result)

if __name__ == "__main__":
    main()
