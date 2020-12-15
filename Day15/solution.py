from copy import deepcopy


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(deepcopy(data)))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    game = [int(num) for num in open(my_file).read().split(',')]
    return game[-1], {num: idx + 1 for idx, num in enumerate(game[:-1])}


def part1(data):
    return memory_game(data[0], data[1])


def part2(data):
    return memory_game(data[0], data[1], 30000000)


def memory_game(current, history, limit=2020):
    for idx in range(len(history) + 1, limit):
        prev_idx = history.get(current, 0)
        history[current] = idx
        current = idx - prev_idx if prev_idx else 0
    return current
