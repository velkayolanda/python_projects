from os.path import join, realpath, dirname

def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

def best_12_digit(line: str) -> int:
    k = 12
    n = len(line)
    result = []

    start = 0
    while k > 0:
        end = n - k
        window = line[start:end+1]
        best_digit = max(window)
        pos = line.index(best_digit, start, end+1)
        result.append(best_digit)
        k -= 1
        start = pos + 1

    return int("".join(result))

def main():
    lines = read_input()
    total = sum(best_12_digit(line) for line in lines)
    print(total)

if __name__ == "__main__":
    main()

