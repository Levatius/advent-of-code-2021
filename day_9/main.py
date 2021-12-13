import numpy as np


def run():
    with open('input.txt') as f:
        heightmap = []
        for line in f.readlines():
            heightmap.append([int(number) for number in line.strip()])
    heightmap = np.asarray(heightmap)

    low_points = part_1(heightmap)
    part_2(heightmap, low_points)


# PART 1

BOUNDARY_POSITION_DELTAS = [np.array([1, 0]), np.array([0, -1]), np.array([-1, 0]), np.array([0, 1])]


def part_1(heightmap):
    low_points = []
    for i, heightrow in enumerate(heightmap):
        for j, height in enumerate(heightrow):
            for boundary_height in get_boundary_heights(heightmap, np.array([i, j])):
                if height >= boundary_height:
                    break
            else:
                low_points.append((i, j))
    risk = sum([heightmap[low_point] + 1 for low_point in low_points])
    print(risk)
    return low_points


def get_boundary_heights(heightmap, position):
    for boundary_position_delta in BOUNDARY_POSITION_DELTAS:
        try:
            boundary_position = tuple(position + boundary_position_delta)
            if boundary_position[0] == -1 or boundary_position[1] == -1:
                # Prevent index wrapping
                continue
            yield heightmap[boundary_position]
        except IndexError:
            # Expected for indices out of range, OK to pass
            pass


# PART 2

BASIN_EDGE_VALUE = 9


def part_2(heightmap, low_points):
    basin_sizes = [len(find_basin(heightmap, low_point)) + 1 for low_point in low_points]
    basin_sizes.sort(reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])


def find_basin(heightmap, low_point):
    basin_points = set()
    for boundary_position_delta in BOUNDARY_POSITION_DELTAS:
        try:
            boundary_position = tuple(low_point + boundary_position_delta)
            if boundary_position[0] == -1 or boundary_position[1] == -1:
                # Prevent index wrapping
                continue
            if heightmap[boundary_position] != BASIN_EDGE_VALUE and heightmap[boundary_position] > heightmap[low_point]:
                basin_points.add(boundary_position)
                basin_points = basin_points.union(find_basin(heightmap, boundary_position))
        except IndexError:
            # Expected for indices out of range, OK to pass
            pass
    return basin_points


if __name__ == '__main__':
    run()
