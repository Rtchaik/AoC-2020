from math import prod


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    # print('Part 2: ', part2(data[1], tuple(data[0]['42']), tuple(data[0]['31'])))


def parse_data(my_file):
    with open(my_file) as f:
        return {int((lines := tile.split('\n'))[0].split()[1][:-1]): lines[1:] for tile in f.read().split('\n\n')}


def part1(data):
    edges = {k: set([v[0], v[-1]] + [''.join(line[idx] for line in v) for idx in (0, len(v[0]) - 1)]) for k, v
             in data.items()}
    neighbours = {k: ({k2 for k2, v2 in edges.items() if v & v2 or v & {x[::-1] for x in v2}} - {k}) for k, v in
                  edges.items()}
    return prod(k for k, v in neighbours.items() if len(v) == 2)


def part2(data):
    return 0
