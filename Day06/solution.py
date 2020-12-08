def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return [[set(item) for item in g]
            for g in map(str.split,
                         open(myFile).read().split('\n\n'))]


def part1(data):
    return counts(data, set.union)


def part2(data):
    return counts(data, set.intersection)


def counts(data, f):
    return sum(len(f(*g)) for g in data)
