from os.path import join, dirname, realpath

def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

def count_accessible_rolls(grid):
    rows, cols = len(grid), len(grid[0])

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        # moja pozicia
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0
            for direct_row, direct_col in directions:
                neigh_row, neigh_col = r + direct_row, c + direct_col
                if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
                    if grid[neigh_row][neigh_col] == '@':
                        neighbors += 1

            if neighbors < 4:
                accessible += 1

    return accessible


if __name__ == "__main__":
    grid = read_input("input.txt")
    result = count_accessible_rolls(grid)
    print("Accessible rolls:", result)
