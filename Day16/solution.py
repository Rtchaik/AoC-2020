import re
from collections import defaultdict
from math import prod


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    data = open(my_file).read().split('\n\n')
    rules = {
        line.split(':')[0]: (set(
            range((ran := [int(num) for num in re.findall(r'\d+', line)])[0], ran[1] + 1)) | set(
            range(ran[2], ran[3] + 1)))
        for line in data[0].splitlines()}
    my_ticket = [int(num) for num in data[1].splitlines()[1].split(',')]
    other_tickets = [[int(num) for num in ticket.split(',')] for ticket in data[2].splitlines()[1:]]
    return rules, my_ticket, other_tickets


def part1(data):
    all_nums = set.union(*data[0].values())
    return sum(sum(set(ticket) - all_nums) for ticket in data[2])


def part2(data):
    all_nums = set.union(*data[0].values())
    valid = [ticket for ticket in data[2] if all_nums.issuperset(ticket)] + [data[1]]
    positions = [[ticket[pos] for ticket in valid] for pos in range(len(valid[0]))]
    result = defaultdict(set)
    for idx, pos in enumerate(positions):
        for rule in data[0]:
            if data[0][rule].issuperset(pos):
                result[idx].add(rule)
    final = {}
    while result:
        final.update({k: v for k, v in result.items() if len(v) == 1})
        result = {k: (v - set.union(*final.values())) for k, v in result.items() if k not in final}
    return prod(data[1][k] for k, v in final.items() if 'departure' in v.pop())
