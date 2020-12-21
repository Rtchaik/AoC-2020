def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(data))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    with open(my_file) as f:
        foods = [(set((part := line.split(' (contains '))[0].split()), set(part[1].strip()[:-1].split(', ')))
                 for line in f.readlines()]
        allergens_draft = {al: set.intersection(*[food[0] for food in foods if al in food[1]])
                           for al in set.union(*[food[1] for food in foods])}
        allergens = {}
        while allergens_draft:
            new = {k: v.pop() for k, v in allergens_draft.items() if len(v) == 1}
            allergens.update(new)
            allergens_draft = {k: v - set(new.values()) for k, v in allergens_draft.items() if len(v) > 1}
        return [food[0] for food in foods], allergens


def part1(data):
    not_allergic = set.union(*data[0]) - set(data[1].values())
    return sum(len(food & not_allergic) for food in data[0])


def part2(data):
    return ','.join(ing for _, ing in sorted(data[1].items()))
