import Day09.solution as current

test1 = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

assert current.part1(test1, 5) == 127

assert current.part2(test1[test1.index(127) - 1::-1], 127) == 62
