def solveDay(myFile):
    data = parseData(myFile)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parseData(myFile):
    return [[tuple(map(int, (line[0].split('-')))), line[1][0], line[2]]
            for line in map(str.split,
                            open(myFile).readlines())]


def part1(data):
    return sum(line[2].count(line[1]) in range(line[0][0], line[0][1] + 1)
               for line in data)


def part2(data):
    return sum(
        sum(line[2][idx] == line[1]
            for idx in (line[0][0] - 1, line[0][1] - 1)) == 1 for line in data)
