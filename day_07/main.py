from math import ceil, floor
from statistics import mean, median


def run():
    with open('input.txt') as f:
        crab_positions = [int(position_str) for position_str in f.readline().split(',')]

    part_1(crab_positions)
    part_2(crab_positions)


# PART 1


def part_1(crab_positions):
    crab_positions_median = round(median(crab_positions))
    total_fuel_cost = 0
    for crab_position in crab_positions:
        total_fuel_cost += abs(crab_position - crab_positions_median)

    print(total_fuel_cost)


# PART 2


def part_2(crab_positions):
    # Direct rounding does not always give the best answer here
    crab_positions_means = [floor(mean(crab_positions)), ceil(mean(crab_positions))]
    for crab_positions_mean in crab_positions_means:
        total_fuel_cost = 0
        for crab_position in crab_positions:
            positions_moved = abs(crab_position - crab_positions_mean)
            total_fuel_cost += int(0.5 * positions_moved * (1 + positions_moved))
        # Use the lower value
        print(total_fuel_cost)


if __name__ == '__main__':
    run()
