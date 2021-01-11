from math import prod
import numpy as np


def solveDay(my_file):
    data = parse_data(my_file)
    result = build_map(data)
    print('Part 1: ', result[0])
    print('Part 2: ', result[1])


def parse_data(my_file):
    with open(my_file) as f:
        return {int((lines := tile.split('\n'))[0].split()[1][:-1]): np.array([[int(y) for y in x] for x in lines[1:]])
                for tile in f.read().replace('.', '0').replace('#', '1').split('\n\n')}


def build_map(data):
    edges = {k: set.union(*[{tuple(edge), tuple(reversed(edge))} for edge in [v[0], v[-1], v[:, 0], v[:, -1]]]) for k, v
             in data.items()}
    neighbours = {k: ({k2 for k2, v2 in edges.items() if v & v2} - {k}) for k, v in edges.items()}
    corners = [k for k in neighbours if len(neighbours[k]) == 2]

    map_final = []
    rev_mode = True
    current = corners[0]
    data[current] = next(tile for tile in rotations(data[current]) if {tuple(tile[:, -1]), tuple(tile[-1])}.issubset(
        set.union(*[edges[x] for x in neighbours[current]])))
    map_row = [data[current][1:-1, 1:-1]]

    def next_tile(adjacent, row=True):
        nonlocal current, map_row
        current = next(tile for tile in neighbours[current] if adjacent in edges[tile])
        data[current] = next(
            tile for tile in rotations(data[current]) if
            adjacent == tuple(tile[:, -(not rev_mode)] if row else tile[0]))
        map_row += [data[current][1:-1, 1:-1]]

    while current:
        try:
            next_tile(tuple(data[current][:, -rev_mode]))
        except StopIteration:
            map_final += [np.hstack(map_row)] if rev_mode else [np.hstack(map_row[::-1])]
            map_row.clear()
            try:
                next_tile(tuple(data[current][-1]), False)
                rev_mode = not rev_mode
            except StopIteration:
                current = None

    map_final = np.vstack(map_final)
    with open(r'Day20/monster') as f:
        monster = np.array([[int(y) for y in x] for x in f.read().replace(' ', '0').replace('#', '1').split()])
    monsters = next(result for my_map in rotations(map_final) if (result := scanner(my_map, monster)) > 0)
    return prod(corners), map_final.sum() - monsters * monster.sum()


def scanner(my_map, monster):
    monsters = 0
    for row in range(2, len(my_map)):
        for col in range(len(my_map) - len(monster[0])):
            area = (my_map[row - 2:row + 1, col:col + len(monster[0])] + monster)
            if len(area[area == 2]) == 15:
                monsters += 1
    return monsters


def rotations(tile):
    for _ in range(2):
        for _ in range(4):
            yield tile
            tile = np.rot90(tile)
        tile = np.flip(tile, 0)
