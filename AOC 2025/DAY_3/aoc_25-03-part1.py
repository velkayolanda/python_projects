from os.path import join, realpath, dirname

def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

def max_two_digit(line: str) -> int:
    best = 0
    n = len(line)
    for i in range(n):
        for j in range(i + 1, n):
            val = int(line[i] + line[j])
            if val > best:
                best = val
    return best

def main():
    lines = read_input()
    total = sum(max_two_digit(line) for line in lines)  # <-- FIXED
    print(total)

if __name__ == "__main__":
    main()