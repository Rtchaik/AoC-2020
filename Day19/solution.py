from itertools import product


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data[1], tuple(data[0]['42']),
                            tuple(data[0]['31'])))


def parse_data(my_file):
    with open(my_file) as f:
        data = f.read().split('\n\n')
        draft_rules = dict(
            rule.split(': ') for rule in data[0].replace('"', '').split('\n'))
        draft_rules = {
            k: [rule.split() for rule in v.split(' | ')]
            for k, v in draft_rules.items()
        }
        rules = {
            k: v[0]
            for k, v in draft_rules.items() if not v[0][0].isdigit()
        }
        messages = data[1].split()
        find_rule(draft_rules, rules, '0')
        return rules, messages


def find_rule(draft, rules, rule):
    if rule in rules:
        return rules[rule]
    else:
        rules[rule] = sum([[
            ''.join(res)
            for res in (product(*[find_rule(draft, rules, c) for c in comb]))
        ] for comb in draft[rule]], [])
        return rules[rule]


def part1(data):
    return sum(mes in data[0]['0'] for mes in data[1])


def part2(messages, *rules):
    count = 0
    for message in messages:
        result = []
        for rule in rules:
            total = 0
            rule_len = len((rule[0]))
            while True:
                if message.startswith(rule):
                    message = message[rule_len:]
                    total += 1
                else:
                    break
            result.append(total)
        if not message and result[0] > result[1] > 0:
            count += 1
    return count
