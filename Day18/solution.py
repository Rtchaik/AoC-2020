from operator import add, mul


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    return open(my_file).readlines()


def part1(data):
    return sum(make_math(line)[0] for line in data)


def part2(data):
    return sum(make_math(line, False)[0] for line in data)


def make_math(expres, mode=True, idx=0, multic=False):
    total = 0
    oper = add
    while idx < len(expres):
        ch = expres[idx]
        if ch == ' ':
            pass
        elif ch.isdigit():
            total = oper(total, int(ch))
        elif ch == '*':
            if mode:
                oper = mul
            elif multic:
                return total, idx - 1
            else:
                subtotal, idx = make_math(expres, mode, idx + 1, True)
                total = mul(total, subtotal)
        elif ch == '+':
            oper = add
        elif ch == '(':
            subtotal, idx = make_math(expres, mode, idx + 1, False)
            total = oper(total, subtotal)
        elif ch == ')':
            if multic:
                return total, idx - 1
            else:
                return total, idx
        idx += 1
    return total, idx
