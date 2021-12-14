from collections import defaultdict


def run():
    with open('input.txt') as f:
        # Read in initial polymer as its pairs and ends
        polymer_pairs = defaultdict(int)
        polymer = f.readline().strip()
        for i in range(len(polymer) - 1):
            polymer_pairs[(polymer[i], polymer[i + 1])] += 1
        polymer_ends = [polymer[0], polymer[-1]]

        # Skip blank line
        f.readline()

        # Create pair to pairs map
        pairs_map = defaultdict(list)
        while line := f.readline().strip():
            pair_str, new_element = line.split(' -> ')
            pair = tuple(pair_element for pair_element in pair_str)
            pairs_map[pair].append((pair[0], new_element))
            pairs_map[pair].append((new_element, pair[1]))

    part_x(polymer_pairs, polymer_ends, pairs_map)
    part_x(polymer_pairs, polymer_ends, pairs_map, steps=40)


# PART 1 AND 2


def part_x(polymer_pairs, polymer_ends, pairs_map, steps=10):
    # Generate polymer
    for _ in range(steps):
        new_polymer_pairs = defaultdict(int)
        for polymer_pair, count in polymer_pairs.items():
            for pair_map in pairs_map[polymer_pair]:
                new_polymer_pairs[pair_map] += count
        polymer_pairs = new_polymer_pairs

    # Count elements
    element_count = defaultdict(int)
    for polymer_pair, count in polymer_pairs.items():
        for element in polymer_pair:
            element_count[element] += count
    for element in element_count:
        # We add the polymer ends here to ensure the division by 2 is clean
        element_count[element] = (element_count[element] + int(element in polymer_ends)) // 2

    print(max(element_count.values()) - min(element_count.values()))


if __name__ == '__main__':
    run()
