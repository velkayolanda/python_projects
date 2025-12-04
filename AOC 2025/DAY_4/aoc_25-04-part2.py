from os.path import join, dirname, realpath

def read_input(file_name="input.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

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

def count_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1
    return count

def remove_accessible_rolls(grid):
    rows, cols = len(grid), len(grid[0])
    marked = []

    # find all removable rolls
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@' and count_neighbors(grid, r, c) < 4:
                marked.append((r, c))

    # convert to list-of-lists for mutation
    new_grid = [list(row) for row in grid]

    # remove them
    for r, c in marked:
        new_grid[r][c] = '.'

    # convert back to list-of-strings
    new_grid = ["".join(row) for row in new_grid]

    return new_grid, len(marked)

def total_removed(grid):
    total = 0

    while True:
        grid, removed = remove_accessible_rolls(grid)
        if removed == 0:
            break
        total += removed

    return total

if __name__ == "__main__":
    grid = read_input("input.txt")
    result = total_removed(grid)
    print("Total rolls removed:", result)
