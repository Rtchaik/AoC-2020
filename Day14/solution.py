import re


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    return [re.findall(r'[X\d]+', line) for line in open(my_file).readlines()]


def part1(data):
    return run_program(data)


def part2(data):
    return run_program(data, False)


def run_program(data, part=True):
    mem = {}
    mask = ''
    for command in data:
        if len(command) == 1:
            mask = command[0]
        else:
            if part:
                mem[command[0]] = decoder(mask, int(command[1]))
            else:
                for address in decoder(mask, int(command[0]), part):
                    mem[address] = int(command[1])
    return sum(mem.values())


def decoder(mask, num, part=True):
    num = bin(num)[2:].zfill(36)
    if part:
        num = ''.join(
            ch if ch != 'X' else num[idx] for idx, ch in enumerate(mask))
        return int(num, 2)
    else:
        num = ''.join(
            str(int(ch) or int(num[idx])) if ch != 'X' else 'X'
            for idx, ch in enumerate(mask))
        return (int(address, 2) for address in addresses(num))


def addresses(num):
    if 'X' not in num:
        return [num]
    else:
        parts = num.split('X', 1)
        return [
            parts[0] + bit + bits for bits in addresses(parts[1])
            for bit in ('0', '1')
        ]
