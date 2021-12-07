from collections import defaultdict
from numpy import array, linspace


def run():
    with open('input.txt') as f:
        line_segments = []
        for line in f.readlines():
            points = []
            for point_str in line.strip().split(' -> '):
                point = array([int(value) for value in point_str.split(',')])
                points.append(point)
            line_segments.append(points)

    part_x([line_segment for line_segment in line_segments if part_1_condition(line_segment)])
    part_x(line_segments)


# PART 1 AND 2

def part_1_condition(line_segment):
    return line_segment[0][0] == line_segment[1][0] or line_segment[0][1] == line_segment[1][1]


def part_x(line_segments):
    vents = defaultdict(int)
    for line_segment in line_segments:
        points_on_line_segment = linspace(*line_segment, number_of_points(line_segment))
        for point in points_on_line_segment:
            vents[sanitise_point(point)] += 1

    overlap_count = sum([1 for value in vents.values() if value > 1])
    print(overlap_count)


def number_of_points(line_segment):
    # Assumes horizontal, vertical or 45 degree lines
    return max(abs(line_segment[0][0] - line_segment[1][0]), abs(line_segment[0][1] - line_segment[1][1])) + 1


def sanitise_point(point):
    # Linspace can return some funky float values over large intervals
    return tuple([round(value) for value in point])


if __name__ == '__main__':
    run()
