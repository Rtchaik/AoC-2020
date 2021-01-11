import Day23.solution as current
from copy import deepcopy

test1 = ((3, 7), {3: 8, 8: 9, 9: 1, 1: 2, 2: 5, 5: 4, 4: 6, 6: 7, 7: 3})

assert current.part1(deepcopy(test1), 10) == '92658374'
assert current.part1(deepcopy(test1), 100) == '67384529'

assert current.part2(test1) == 149245887792
