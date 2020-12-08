import re


def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    bags = (re.findall(r'(\d?\s?\w+\s\w+)\sbag', line)
            for line in open(myFile).readlines())
    return {
        bag[0]:
        dict(reversed(item.split(maxsplit=1))
             for item in bag[1:]) if not bag[1].endswith('other') else {}
        for bag in bags
    }


def part1(data):
    current = {'shiny gold'}
    total = set()
    while current:
        current = {k for k, v in data.items() if v.keys() & current}
        total |= current
    return len(total)


def part2(data, current='shiny gold'):
    return sum(int(v) * (1 + part2(data, k)) for k, v in data[current].items())
