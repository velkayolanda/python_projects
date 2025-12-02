from os.path import join, realpath, dirname

def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

def simulate(rotations):
    position = 50
    zero_count = 0

    for rot in rotations:
        direction = rot[0]
        distance = int(rot[1:])

        if direction == "L":
            position = (position - distance) % 100
        else:  # "R"
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count

def main():
    rotations = read_input()
    password = simulate(rotations)
    print("Password:", password)

if __name__ == "__main__":
    main()
