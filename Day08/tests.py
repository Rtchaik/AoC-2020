import Day08.solution as current

test1 = [['nop', 0], ['acc', 1], ['jmp', 4], ['acc', 3], ['jmp', -3],
         ['acc', -99], ['acc', 1], ['jmp', -4], ['acc', 6]]

assert current.part1(test1)[0] == 5

assert current.part2(test1) == 8
