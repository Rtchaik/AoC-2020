def solveDay(myFile):
    data = parseData(myFile)
    ids = sorted(seat(num) for num in data)
    print('Part 1: ', ids[-1])
    print('Part 2: ', part2(ids))


def parseData(myFile):
    return map(str.strip, open(myFile).readlines())


def part2(data):
    return (set(range(data[0], data[-1])) - set(data)).pop()


def seat(b_pas):
    return bin_search(b_pas[:7]) * 8 + bin_search(b_pas[7:], 7)


def bin_search(b_pas, max_seat=127):
    min_seat = 0
    sector = max_seat + 1
    for ch in b_pas:
        sector //= 2
        if ch in 'FL':
            max_seat -= sector
        else:
            min_seat += sector
    return min_seat
