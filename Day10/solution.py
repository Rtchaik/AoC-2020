from itertools import groupby
from collections import defaultdict
from operator import sub
from math import prod


def solveDay(myFile):
    data = parse_data(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(myFile):
    return group_and_count(
        sorted(int(line) for line in open(myFile).readlines()))


def group_and_count(adapters):
    return [[k, len(list(g))] for k, g in groupby(
        sub(*pair) for pair in zip(adapters, [0] + adapters))] + [[3, 1]]


def part1(data):
    result = defaultdict(int)
    for item in data:
        result[item[0]] += item[1]
    return prod(result.values())


def part2(data):
    tribonnacci = (1, 1, 2, 4, 7)
    return prod(tribonnacci[num[1]] for num in data if num[0] == 1)
