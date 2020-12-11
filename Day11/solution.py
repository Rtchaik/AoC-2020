def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    return [line.strip() for line in open(my_file).readlines()]


def part1(data):
    return equilibrium_seats(data)


def part2(data):
    return equilibrium_seats(data, 4, False)


def equilibrium_seats(state, min_occ=3, level_1=True):
    max_row, max_col = len(state), len(state[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

    def occupied(ferry, row, col):
        def next_seat(direct):
            new_row, new_col = row, col
            while True:
                new_row += direct[0]
                new_col += direct[1]
                if new_row < 0 or new_row >= max_row or new_col < 0 or new_col >= max_col:
                    return '.'
                elif (seat := ferry[new_row][new_col]) in 'L#' or level_1:
                    return seat

        return sum(next_seat(dr) == '#' for dr in dirs)

    old_state = []
    while old_state != state:
        old_state = state
        state = []
        for cur_row in range(max_row):
            new_line = ''
            for cur_col in range(max_col):
                current = old_state[cur_row][cur_col]
                occ = occupied(old_state, cur_row, cur_col)
                if current == 'L' and occ == 0:
                    new_line += '#'
                elif current == '#' and occ > min_occ:
                    new_line += 'L'
                else:
                    new_line += current
            state.append(new_line)

    return sum(row.count('#') for row in state)
