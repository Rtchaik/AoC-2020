from itertools import combinations
from math import prod


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return tuple(map(int, open(myFile).readlines()))


def part1(data):
    return multic(data, 2)


def part2(data):
    return multic(data, 3)


def multic(data, r):
    return prod(
        next(comb for comb in combinations(data, r) if sum(comb) == 2020))
