def run():
    with open('input.txt') as f:
        commands = []
        for line in f.readlines():
            direction, units = line.strip().split(' ')
            command = direction, int(units)
            commands.append(command)

    part_1(commands)
    part_2(commands)


# PART 1

FORWARD = 'forward'
DOWN = 'down'
UP = 'up'


def part_1(commands):
    horizontal_position = 0
    depth = 0
    for command in commands:
        direction, units = command
        if direction == FORWARD:
            horizontal_position += units
        elif direction == DOWN:
            depth += units
        elif direction == UP:
            depth -= units
    print(horizontal_position, depth, horizontal_position * depth)

# PART 2


def part_2(commands):
    horizontal_position = 0
    depth = 0
    aim = 0
    for command in commands:
        direction, units = command
        if direction == FORWARD:
            horizontal_position += units
            depth += aim * units
        elif direction == DOWN:
            aim += units
        elif direction == UP:
            aim -= units
    print(horizontal_position, depth, horizontal_position * depth)


if __name__ == '__main__':
    run()
