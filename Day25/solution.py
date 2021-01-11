from itertools import count


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))


def parse_data(my_file):
    with open(my_file) as f:
        return {int(num) for num in f.readlines()}


def part1(data):
    num = 1
    div = 20201227
    for loop in count(1):
        if (num := num * 7 % div) in data:
            return pow((data - {num}).pop(), loop, div)
