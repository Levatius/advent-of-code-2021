import numpy as np
from copy import copy


def run():
    with open('input.txt') as f:
        octopus_grid = []
        for line in f.readlines():
            octopus_grid.append([int(number) for number in line.strip()])
    octopus_grid = np.asarray(octopus_grid)

    part_x(copy(octopus_grid), steps=100)
    part_x(copy(octopus_grid))


# PART 1 AND 2

FLASH_ENERGY_LEVEL = 9
RESET_ENERGY_LEVEL = 0
ADJACENT_POSITION_DELTAS = [np.array([1, 0]), np.array([1, -1]), np.array([0, -1]), np.array([-1, -1]),
                            np.array([-1, 0]), np.array([-1, 1]), np.array([0, 1]), np.array([1, 1])]


def part_x(octopus_grid, steps=1000):
    flashes = 0
    flash_positions = set()
    for step in range(steps):
        # Increase the energy of every octopus by 1
        octopus_grid += 1

        # Flash any octopus with high enough energy level
        for i, octopus_row in enumerate(octopus_grid):
            for j, _ in enumerate(octopus_row):
                flash(octopus_grid, (i, j), flash_positions)

        # For Part 2, check when a simultaneous flash occurs
        if len(flash_positions) == octopus_grid.size:
            print(step + 1)
            break

        # Reset any octopus that flashed
        while len(flash_positions) > 0:
            flash_position = flash_positions.pop()
            octopus_grid[flash_position] = RESET_ENERGY_LEVEL
            flashes += 1
    else:
        print(flashes)


def get_adjacent_positions(octopus_grid, position):
    for adjacent_position_delta in ADJACENT_POSITION_DELTAS:
        adjacent_position = tuple(np.array(position) + adjacent_position_delta)
        if adjacent_position[0] in (-1, octopus_grid.shape[0]) or adjacent_position[1] in (-1, octopus_grid.shape[1]):
            # Prevent out of bounds
            continue
        yield adjacent_position


def flash(octopus_grid, position, flash_positions):
    octopus = octopus_grid[position]
    if not octopus > FLASH_ENERGY_LEVEL or position in flash_positions:
        # Cancel flash
        return
    flash_positions.add(position)

    for adjacent_position in get_adjacent_positions(octopus_grid, position):
        octopus_grid[adjacent_position] += 1
        flash(octopus_grid, adjacent_position, flash_positions)


if __name__ == '__main__':
    run()
