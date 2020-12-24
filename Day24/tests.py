import Day24.solution as current

test1 = {(-3, 2), (-3, 3), (-2, 0), (0, -1), (-2, 1), (3, -3), (0, 2), (0, 0), (2, 0), (-1, -1)}

assert current.part1(test1) == 10

assert current.part2(test1) == 2208
