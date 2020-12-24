from collections import Counter


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    flips = []
    with open(my_file) as f:
        for line in f.readlines():
            q, r = 0, 0
            vector = ''
            for ch in line.strip():
                if ch in 'sn':
                    vector = ch
                else:
                    vector += ch
                    if vector in 'ew':
                        q += -1 if vector == 'w' else 1
                    elif vector in ('nw', 'se'):
                        r += -1 if vector == 'nw' else 1
                    else:
                        if vector == 'ne':
                            q += 1
                            r -= 1
                        else:
                            q -= 1
                            r += 1
                    vector = ''
            flips.append((q, r))
        return {tile for tile, turns in Counter(flips).items() if turns % 2}


def part1(data):
    return len(data)


def part2(black):
    directions = ((1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1))
    for _ in range(100):
        new = set()
        nb = set()
        for tile in black:
            neighb = neighbors(tile, directions)
            nb |= neighb
            if len(neighb & black) in (1, 2):
                new |= {tile}
        black = new | {
            tile
            for tile in nb - black
            if len(neighbors(tile, directions) & black) == 2
        }
    return len(black)


def neighbors(tile, directions):
    return {(tile[0] + q, tile[1] + r) for q, r in directions}
