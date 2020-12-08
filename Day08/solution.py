def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data)[0])
    print('Part 2: ', part2(data))


def parseData(myFile):
    return [[op, int(num)] for op, num in map(str.split,
                                              open(myFile).readlines())]


def part1(data):
    idx = 0
    accumulator = 0
    visited = {0}
    while idx < len(data):
        if data[idx][0] == 'jmp':
            idx += data[idx][1]
        else:
            if data[idx][0] == 'acc':
                accumulator += data[idx][1]
            idx += 1
        if idx in visited:
            return accumulator, False
        else:
            visited.add(idx)
    return accumulator, True


def part2(data):
    change = {'jmp': 'nop', 'nop': 'jmp'}
    for idx in range(len(data)):
        current = data[idx]
        if current[0] in change:
            current[0] = change[current[0]]
            test = part1(data)
            if test[1]:
                return test[0]
            current[0] = change[current[0]]
