import Day02.solution as current

test1 = [[(1, 3), 'a', 'abcde'], [(1, 3), 'b', 'cdefg'],
         [(2, 9), 'c', 'ccccccccc']]

assert current.part1(test1) == 2

assert current.part2(test1) == 1
