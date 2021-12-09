from collections import defaultdict


def run():
    with open('input.txt') as f:
        entries = []
        for line in f.readlines():
            input_values_str, output_values_str = line.strip().split(' | ')
            entry = input_values_str.split(' '), output_values_str.split(' ')
            entries.append(entry)

    part_1(entries)
    part_2(entries)


# PART 1

VALID_LENGTHS = (2, 4, 3, 7)


def part_1(entries):
    valid_count = 0
    for entry in entries:
        _, output_values = entry
        for output_value in output_values:
            valid_count += int(len(output_value) in VALID_LENGTHS)
    print(valid_count)


# PART 2

TOP_SECRET_DECODE_MAP = {
    42: 0,
    17: 1,
    34: 2,
    39: 3,
    30: 4,
    37: 5,
    41: 6,
    25: 7,
    49: 8,
    45: 9
}


def part_2(entries):
    decoded_total = 0
    for entry in entries:
        input_values, output_values = entry

        segment_counts = defaultdict(int)
        for input_value in input_values:
            for segment in input_value:
                segment_counts[segment] += 1

        decoded_output_values = [decoder(segment_counts, output_value) for output_value in output_values]
        decoded_number = int(''.join(decoded_output_values))
        decoded_total += decoded_number
    print(decoded_total)


def decoder(segment_counts, output_value):
    output_value_sum = sum([segment_counts[segment] for segment in output_value])
    return str(TOP_SECRET_DECODE_MAP[output_value_sum])


if __name__ == '__main__':
    run()
