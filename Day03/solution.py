from math import prod


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data, 3, 1))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return list(map(str.strip, open(myFile).readlines()))


def part1(data, right, down):
    return sum(line[idx * right % len(line)] == '#'
               for idx, line in enumerate(data[::down]))


def part2(data):
    return prod(
        part1(data, *slope)
        for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))
