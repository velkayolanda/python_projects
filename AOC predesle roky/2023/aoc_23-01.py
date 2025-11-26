from os.path import join, realpath, dirname

def read_input(file_name="trebuchet.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

def main():
    slova = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]

    lines = read_input()  # reads trebuchet.txt next to this script
    total = 0

    for line in lines:
        digits = []

        for i, ch in enumerate(line):
            if ch.isdigit():
                digits.append(int(ch))

            for d, word in enumerate(slova):
                if line.startswith(word, i):
                    digits.append(d)
                    break

        if digits:
            total += digits[0] * 10 + digits[-1]

    print("Total:", total)


if __name__ == "__main__":
    main()
