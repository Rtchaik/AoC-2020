def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    return open(my_file).readlines()


def part1(instructions):
    return travel(instructions)


def part2(instructions):
    return travel(instructions, 0)


def travel(instructions, mode=1):
    dirs = 'ESWN'
    direction = 0
    wp = [0, 0] if mode else [1, 10]
    ship = [0, 0]
    for instr in instructions:
        act, val = instr[0], int(instr[1:].strip())
        if act == 'F':
            if mode:
                act = dirs[direction]
            else:
                ship = [ship[num] + wp[num] * val for num in (0, 1)]
                continue
        if act in 'RL':
            idx = (-1)**'RL'.index(act) * val // 90 % 4
            if mode:
                direction = (direction + idx) % 4
            else:
                wp = [(0, -1)[idx == 2] * wp[num] -
                      (-1)**num * (2 - idx) * wp[not num] for num in (0, 1)]
        else:
            wp[act in 'EW'] += (-1)**('NS', 'EW')[act in 'EW'].index(act) * val
    return sum(abs(coord) for coord in (wp if mode else ship))
