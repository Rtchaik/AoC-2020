from itertools import product


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    return {(x, y)
            for y, row in enumerate(open(my_file).readlines())
            for x, ch in enumerate(row) if ch == '#'}


def part1(data):
    return run_cycles({cube + (0, ) for cube in data}, 3)


def part2(data):
    return run_cycles({cube + (0, 0) for cube in data}, 4)


def run_cycles(cubes, dims):
    for _ in range(6):
        new = set()
        nb = set()
        for cube in cubes:
            neighb = neighbors(cube, dims)
            nb |= neighb
            if len(neighb & cubes) in (2, 3):
                new |= {cube}
        cubes = new | {
            cube
            for cube in nb - cubes if len(neighbors(cube, dims) & cubes) == 3
        }
    return len(cubes)


def neighbors(cube, dims):
    return set(
        product(*[range(cube[idx] - 1, cube[idx] + 2)
                  for idx in range(dims)])) - {cube}
