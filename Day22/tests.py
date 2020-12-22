import Day22.solution as current
from collections import deque
from copy import deepcopy

test1 = [deque([9, 2, 6, 3, 1]), deque([5, 8, 4, 7, 10])]

assert current.part1(deepcopy(test1)) == 306

assert current.part2(test1) == 291
