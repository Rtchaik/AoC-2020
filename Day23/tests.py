import Day23.solution as current
from copy import deepcopy
from collections import deque

test1 = deque([3, 8, 9, 1, 2, 5, 4, 6, 7])

assert current.part1(deepcopy(test1), 10) == '92658374'
assert current.part1(deepcopy(test1), 100) == '67384529'
#
# assert current.part2(test1) == 291
