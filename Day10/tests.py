import Day10.solution as current

test1 = current.group_and_count([1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19])
test2 = current.group_and_count([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24,
                                 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49])

assert current.part1(test1) == 35
assert current.part1(test2) == 220

assert current.part2(test1) == 8
assert current.part2(test2) == 19208
