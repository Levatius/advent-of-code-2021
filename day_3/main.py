def run():
    with open('input.txt') as f:
        binaries = [line.strip() for line in f.readlines()]

    part_1(binaries)
    part_2(binaries)


# PART 1


def part_1(binaries):
    # Assuming all binaries are the same length
    binary_length = len(binaries[0])

    gamma_rate = ''
    for index in range(binary_length):
        bit_column = [int(binary[index]) for binary in binaries]
        bit_column_mode = round(sum(bit_column) / len(bit_column))
        gamma_rate += str(bit_column_mode)

    # Invert the gamma rate to get the epsilon rate
    epsilon_rate = ''.join([str(int(not int(gamma_bit))) for gamma_bit in gamma_rate])

    gamma_rate_decimal = int(gamma_rate, 2)
    epsilon_rate_decimal = int(epsilon_rate, 2)

    print(gamma_rate, epsilon_rate, gamma_rate_decimal * epsilon_rate_decimal)


# PART 2

# When the mode is both 0 and 1, the sum over length ratio is 0.5
MODE_EQUALITY_RATIO = 0.5


def part_2(binaries):
    oxygen_generator_rating = find_rating(binaries, mode_equality_value=1)
    co2_scrubber_rating = find_rating(binaries, mode_equality_value=0)

    oxygen_generator_rating_decimal = int(oxygen_generator_rating, 2)
    co2_scrubber_rating_decimal = int(co2_scrubber_rating, 2)

    print(oxygen_generator_rating, co2_scrubber_rating, oxygen_generator_rating_decimal * co2_scrubber_rating_decimal)


def find_rating(binaries, mode_equality_value, index=0):
    if len(binaries) == 1:
        return binaries[0]

    bit_column = [int(binary[index]) for binary in binaries]
    bit_column_ratio = sum(bit_column) / len(bit_column)
    bit_column_mode = round(bit_column_ratio)

    reduced_binaries = []

    for binary in binaries:
        bit = int(binary[index])
        if bit_column_ratio == MODE_EQUALITY_RATIO:
            if bit == mode_equality_value:
                reduced_binaries.append(binary)
        else:
            if bool(mode_equality_value) == (bit == bit_column_mode):
                reduced_binaries.append(binary)

    return find_rating(reduced_binaries, mode_equality_value, index=index + 1)


if __name__ == '__main__':
    run()
