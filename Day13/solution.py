from itertools import count
from operator import mul


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data[1]))


def parse_data(my_file):
    data = open(my_file).readlines()
    return int(data[0].strip()), {
        int(bus): idx
        for idx, bus in enumerate(data[1].split(',')) if bus != 'x'
    }


def part1(data):
    return mul(*min([-data[0] % bus, bus] for bus in data[1]))


def part2(buses):
    start_idx, steps = 0, 1
    for bus, offset in sorted(buses.items(), reverse=True):
        for tstamp in count(start_idx, steps):
            if not (tstamp + offset) % bus:
                start_idx = tstamp
                steps *= bus
                break
    return tstamp
