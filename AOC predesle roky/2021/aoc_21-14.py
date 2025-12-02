from os.path import dirname, join, realpath
from collections import Counter, defaultdict


def read_input(file_name="polymers.txt"):
    file_path = join(dirname(realpath(__file__)), file_name)
    with open(file_path, "r") as file:
        return file.read().splitlines()

def parse_input(lines):
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        pair, insert = line.split("->")
        rules[pair.strip()] = insert.strip()
    return template, rules

def apply_rules(template, rules, steps):
    polymer = template
    for _ in range(steps):
        new_polymer = []
        for i in range(len(polymer) - 1):
            pair = polymer[i:i+2]
            new_polymer.append(polymer[i])
            if pair in rules:
                new_polymer.append(rules[pair])
        new_polymer.append(polymer[-1]  )
        polymer = "".join(new_polymer)
    return polymer

def difference(polymer):
    counts = Counter(polymer)
    return max(counts.values()) - min(counts.values())

def apply_rules_for_counts(template, rules, steps):
    pair_counts = defaultdict(int)

    for i in range(len(template) - 1):
        pair_counts[template[i:i+2]] += 1

    for _ in range(steps):
        new_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            if pair in rules:
                insert = rules[pair]
                new_counts[pair[0] + insert] += count
                new_counts[insert + pair[1]] += count
            else:
                new_counts[pair] += count
        pair_counts = new_counts

    letter_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        letter_counts[pair[0]] += count
    letter_counts[template[-1]] += 1

    return letter_counts

def main():
    lines = read_input()
    template, rules = parse_input(lines)
    polymer = apply_rules(template, rules, steps=10)
    print("rozdil medzi min a max: ", difference(polymer), "\n")
    polymer = apply_rules_for_counts(template, rules, steps = 40)
    print("rozdil medzi najcastejsie a nejmenej caste: ", max(polymer.values()) - min(polymer.values()))


if __name__ == "__main__":
    main()
