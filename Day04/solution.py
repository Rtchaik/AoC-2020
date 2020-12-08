def solveDay(myFile):
    data = parseData(myFile)
    valid = part1(data)
    print('Part 1: ', len(valid))
    print('Part 2: ', part2(valid))


def parseData(myFile):
    return [dict(entry.split(':') for entry in pas.split()) for pas in open(myFile).read().split('\n\n')]


def part1(data):
    fields = {'ecl', 'eyr', 'byr', 'pid', 'hcl', 'iyr', 'hgt'}
    return [pas for pas in data if fields <= set(pas.keys())]


def part2(data):
    return sum(is_valid_pas(pas) for pas in data)


def is_valid_pas(pas):
    return all((1920 <= int(pas['byr']) <= 2002,
                2010 <= int(pas['iyr']) <= 2020,
                2020 <= int(pas['eyr']) <= 2030,
                valid_height(pas['hgt']),
                (v := pas['hcl']).startswith('#') and len(v) == 7 and
                all(ch.isdigit() or ch in 'abcdef' for ch in v[1:]),
                pas['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
                len(pas['pid']) == 9 and pas['pid'].isdigit()))


def valid_height(height):
    if height.endswith('cm'):
        return 150 <= int(height[:-2]) <= 193
    elif height.endswith('in'):
        return 59 <= int(height[:-2]) <= 76
    else:
        return False
