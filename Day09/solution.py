def solveDay(myFile):
    data = parseData(myFile)
    invalid = part1(data)
    print('Part 1: ', invalid)
    print('Part 2: ', part2(data[data.index(invalid) - 1::-1], invalid))


def parseData(myFile):
    return [int(line) for line in open(myFile).readlines()]


def part1(data, preamble=25):
    for idx, num in enumerate(data[preamble:]):
        preamble_data = data[idx:idx + preamble]
        while preamble_data:
            if num - preamble_data.pop() in preamble_data:
                break
        if not preamble_data:
            return num
    raise Exception('Unsolvable part1')


def part2(data, invalid):
    for idx_start in range(len(data) - 1):
        total = invalid - data[idx_start]
        for idx_end in range(idx_start + 1, len(data)):
            total -= data[idx_end]
            if total == 0:
                final_range = sorted(data[idx_start:idx_end + 1])
                return final_range[0] + final_range[-1]
            elif total < 0:
                break
    raise Exception('Unsolvable part2')
