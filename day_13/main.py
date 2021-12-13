def run():
    with open('input.txt') as f:
        spots = set()
        while line := f.readline().strip():
            spot = tuple(int(value) for value in line.split(','))
            spots.add(spot)
        folds = []
        while line := f.readline().strip():
            axis, value = line.lstrip('fold along ').split('=')
            fold = int(value) if axis == 'x' else None, int(value) if axis == 'y' else None
            folds.append(fold)

    part_x(spots, folds)


# PART 1 AND 2


def part_x(spots, folds):
    for i, fold in enumerate(folds):
        fold_x, fold_y = fold
        new_spots = set()
        for spot in spots:
            spot_x, spot_y = spot
            if fold_x and spot_x > fold_x:
                new_spots.add((2 * fold_x - spot_x, spot_y))
            elif fold_y and spot_y > fold_y:
                new_spots.add((spot_x, 2 * fold_y - spot_y))
            else:
                new_spots.add(spot)
        spots = new_spots

        # Part 1, print number of spots after a single fold
        if i == 0:
            print(len(spots))
    print_spots(spots)


def print_spots(spots):
    for j in range(max([y for _, y in spots]) + 1):
        row = ''
        for i in range(max([x for x, _ in spots]) + 1):
            row += '#' if (i, j) in spots else ' '
        print(row)


if __name__ == '__main__':
    run()
