from copy import deepcopy
from operator import mul


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(deepcopy(data), 100))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    with open(my_file) as f:
        cups = [int(ch) for ch in f.read()]
        return (cups[0], cups[-1]), dict(
            pair for pair in zip(cups, cups[1:] + [cups[0]]))


def part1(data, moves):
    return ''.join(str(num) for num in game(data[0][0], data[1], moves, 9))


def part2(data):
    data[1][data[0][1]] = 10
    data[1][1000000] = data[0][0]
    data[1].update({num: num + 1 for num in range(10, 1000000)})
    return mul(*(game(data[0][0], data[1], 10000000, 1000000)[:2]))


def game(current, cups, moves, max_cup):
    for _ in range(moves):
        next_cup = current
        picks = []
        for _ in range(3):
            next_cup = cups[next_cup]
            picks.append(next_cup)
        dest = next(destination(picks, current, max_cup))
        cups[current] = cups[next_cup]
        cups[next_cup] = cups[dest]
        cups[dest] = picks[0]
        current = cups[current]
    next_cup = 1
    picks = []
    for _ in range(8):
        next_cup = cups[next_cup]
        picks.append(next_cup)
    return picks


def destination(picks, current, max_cup):
    while True:
        current -= 1
        if current == 0:
            current = max_cup
        if current not in picks:
            yield current
