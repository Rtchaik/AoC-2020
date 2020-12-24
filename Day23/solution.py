from collections import deque
from copy import deepcopy
from operator import mul


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(deepcopy(data), 100))
    # print('Part 2: ', part2(data))


def parse_data(my_file):
    with open(my_file) as f:
        return deque(int(ch) for ch in f.read())


def part1(data, moves):
    return ''.join(str(num) for num in game(data, moves, 9))


def part2(data):
    data.extend(range(10, 1001))
    data = game(data, 10000, 1000)
    return mul(*([data.popleft() for _ in range(3)][1:]))


def game(data, moves, max_cup):
    data.rotate(-1)
    for _ in range(moves):
        current = data[-1]
        picks = [data.popleft() for _ in range(3)]
        dest = data.index(next(destination(picks, current, max_cup)))
        data.rotate(-dest - 1)
        data.extend(picks)
        data.rotate(dest + 3)
        # try:
        #     idx = data.index(1)
        #     print(data[idx + 1], data[idx + 2])
        # except:
        #     print()
    data.rotate(-data.index(1))
    data.popleft()
    return data


def destination(picks, current, max_cup):
    while True:
        current -= 1
        if current == 0:
            current = max_cup
        if current not in picks:
            yield current

# def part11(data, moves):
#     for _ in range(moves):
#         new = data[4:] + [data[0]]
#         dest = new.index(next(destination(new))) + 1
#         data = new[:dest] + data[1:4] + new[dest:]
#     data = data[(idx := data.index(1)) + 1:] + data[:idx]
#     return ''.join(str(num) for num in data)
#
#
# def destination11(data):
#     for idx in range(1, 10):
#         dif = data[-1] - idx
#         dest = dif if dif > 0 else dif + 9
#         if dest in data:
#             yield dest
