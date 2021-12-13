from collections import Counter
from copy import copy
from networkx import Graph


def run():
    with open('input.txt') as f:
        caves = Graph()
        for line in f.readlines():
            caves.add_edge(*line.strip().split('-'))

    part_x(caves, small_cave_repeat_limit=0)
    part_x(caves, small_cave_repeat_limit=1)


# PART 1 AND 2

START_CAVE = 'start'
END_CAVE = 'end'


def part_x(caves, small_cave_repeat_limit):
    start_path = [START_CAVE]
    complete_paths = generate_paths(caves, start_path, small_cave_repeat_limit)
    print(len(complete_paths))


def generate_paths(caves, path, small_cave_repeat_limit):
    complete_paths = []
    for connected_cave in caves[path[-1]]:
        if connected_cave == START_CAVE:
            continue
        elif connected_cave == END_CAVE:
            complete_path = copy(path)
            complete_path.append(connected_cave)
            complete_paths.append(complete_path)
        elif check_small_cave_repeat_condition(path, connected_cave, small_cave_repeat_limit):
            continue
        else:
            new_path = copy(path)
            new_path.append(connected_cave)
            complete_paths += generate_paths(caves, new_path, small_cave_repeat_limit)
    return complete_paths


def check_small_cave_repeat_condition(path, connected_cave, small_cave_repeat_limit):
    visit_counts = Counter(path)
    visit_counts[connected_cave] += 1
    small_cave_repeats = sum([visit_count - 1 for cave, visit_count in visit_counts.items() if cave.islower()])
    return small_cave_repeats > small_cave_repeat_limit


if __name__ == '__main__':
    run()
