from statistics import median


def run():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    part_1(lines)
    part_2(lines)


# PART 1

CHUNK_SYMBOL_MAPPING = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

ERROR_SYMBOL_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def part_1(lines):
    error_score = 0
    for line in lines:
        error_symbol, _ = find_error_symbol(line)
        if error_symbol:
            error_score += ERROR_SYMBOL_SCORES[error_symbol]
    print(error_score)


def find_error_symbol(line):
    open_chunks = []
    for symbol in line:
        if symbol in CHUNK_SYMBOL_MAPPING.keys():
            open_chunks.append(symbol)
        elif symbol == CHUNK_SYMBOL_MAPPING[open_chunks[-1]]:
            open_chunks.pop()
        else:
            return symbol, open_chunks
    return None, open_chunks


# PART 2

AUTOCOMPLETE_SYMBOL_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def part_2(lines):
    autocomplete_scores = []
    for line in lines:
        error_symbol, open_chunks = find_error_symbol(line)
        if not error_symbol:
            autocomplete_scores.append(convert_open_chunks_to_autocomplete_score(open_chunks))
    print(median(autocomplete_scores))


def convert_open_chunks_to_autocomplete_score(open_chunks):
    autocomplete_score = 0
    while len(open_chunks) > 0:
        symbol = open_chunks.pop()
        autocomplete_score = 5 * autocomplete_score + AUTOCOMPLETE_SYMBOL_SCORES[CHUNK_SYMBOL_MAPPING[symbol]]
    return autocomplete_score


if __name__ == '__main__':
    run()
