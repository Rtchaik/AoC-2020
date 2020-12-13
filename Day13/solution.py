from itertools import count


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    data = open(my_file).readlines()
    return int(data[0].strip()), {
        int(bus): idx
        for idx, bus in enumerate(data[1].split(',')) if bus != 'x'
    }


def part1(data):
    for idx in count(1):
        for bus in data[1].keys():
            if not (data[0] + idx) % bus:
                return idx * bus


def part2(data):
    nums = sorted(data[1].keys(), reverse=True)
    start_idx, st = 1, 1
    for current in nums[1:]:
        shift = (data[1][nums[0]] - data[1][current]) % current
        for idx in count(start_idx, st):
            if (nums[0] * idx) % current == shift:
                start_idx = idx
                st *= current
                break
    return nums[0] * start_idx - data[1][nums[0]]
