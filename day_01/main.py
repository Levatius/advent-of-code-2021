def run():
    with open('input.txt') as f:
        depths = [int(line.strip()) for line in f.readlines()]

    part_1(depths)
    part_2(depths)


# PART 1

def part_1(depths):
    depth_increases = 0
    previous_depth = None
    for depth in depths:
        if previous_depth and depth > previous_depth:
            depth_increases += 1
        previous_depth = depth
    print(depth_increases)


# PART 2
WINDOW_LENGTH = 3


def part_2(depths):
    depth_increases = 0
    for index in range(WINDOW_LENGTH + 1, len(depths) + 1):
        previous_index = index - 1
        previous_window = depths[previous_index - WINDOW_LENGTH:previous_index]
        current_window = depths[index - WINDOW_LENGTH:index]
        if sum(current_window) > sum(previous_window):
            depth_increases += 1
    print(depth_increases)


if __name__ == '__main__':
    run()
