from collections import defaultdict


def run():
    with open('input.txt') as f:
        fish_counts = defaultdict(int)
        for initial_timer_str in f.readline().strip().split(','):
            fish_counts[int(initial_timer_str)] += 1

    part_x(fish_counts)
    part_x(fish_counts, total_days=256)


# PART 1 AND 2

NEW_FISH_INITIAL_TIMER = 8
CREATE_FISH_TIME = 0
CREATE_FISH_RESET_TIMER = 6


def part_x(fish_counts, total_days=80):
    for _ in range(total_days):
        new_fish_counts = defaultdict(int)
        for time, fish_count in fish_counts.items():
            if time != CREATE_FISH_TIME:
                new_fish_counts[time - 1] += fish_count
            else:
                new_fish_counts[CREATE_FISH_RESET_TIMER] += fish_count
                new_fish_counts[NEW_FISH_INITIAL_TIMER] += fish_count
        fish_counts = new_fish_counts

    print(sum(fish_counts.values()))


if __name__ == '__main__':
    run()
