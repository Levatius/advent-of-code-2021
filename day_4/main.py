from copy import deepcopy


def run():
    with open('input.txt') as f:
        drawn_numbers = [int(number) for number in f.readline().strip().split(',')]
        bingo_sheets = []
        j = 0
        for line in f.readlines():
            line = line.strip()
            if not line:
                bingo_sheets.append({})
                j = 0
            else:
                bingo_sheet_row = {int(number): {f'h{i}': False, f'v{j}': False} for i, number in
                                   enumerate(line.split())}
                bingo_sheets[-1] |= bingo_sheet_row
                j += 1

    part_1(drawn_numbers, deepcopy(bingo_sheets))
    part_2(drawn_numbers, deepcopy(bingo_sheets))


# PART 1

def part_1(drawn_numbers, bingo_sheets):
    for drawn_number in drawn_numbers:
        for bingo_sheet in bingo_sheets:
            if drawn_number in bingo_sheet:
                mark_number(bingo_sheet, drawn_number)
                if check_win_condition(bingo_sheet, drawn_number):
                    print(sum_unmarked_numbers(bingo_sheet) * drawn_number)
                    return


def mark_number(bingo_sheet, drawn_number):
    # Mark both the horizontal and vertical positions
    for position in bingo_sheet[drawn_number]:
        bingo_sheet[drawn_number][position] = True


def check_win_condition(bingo_sheet, drawn_number):
    # Check both the horizontal and vertical win conditions
    for position in bingo_sheet[drawn_number]:
        # Check each number in the bingo sheet
        for number, position_data in bingo_sheet.items():
            # If the number is in a relevant position to the drawn number
            if position in position_data:
                # If the number has not been marked, stop searching this win condition
                if not position_data[position]:
                    break
        else:
            # If all relevant numbers have been checked and none of them stopped the search
            return True
    return False


def sum_unmarked_numbers(bingo_sheet):
    total = 0
    for number in bingo_sheet:
        for position in bingo_sheet[number]:
            if bingo_sheet[number][position]:
                break
        else:
            total += number
    return total


# PART 2


def part_2(drawn_numbers, bingo_sheets):
    for drawn_number in drawn_numbers:
        bingo_sheets_marked_for_removal = []
        for bingo_sheet in bingo_sheets:
            if drawn_number in bingo_sheet:
                mark_number(bingo_sheet, drawn_number)
                if check_win_condition(bingo_sheet, drawn_number):
                    if len(bingo_sheets) > 1:
                        bingo_sheets_marked_for_removal.append(bingo_sheet)
                    else:
                        print(sum_unmarked_numbers(bingo_sheet) * drawn_number)
                        return
        # Remove bingo sheets that have already won
        for bingo_sheet in bingo_sheets_marked_for_removal:
            bingo_sheets.remove(bingo_sheet)


if __name__ == '__main__':
    run()
