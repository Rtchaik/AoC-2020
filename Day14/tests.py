import Day14.solution as current

test1 = [['XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'], ['8', '11'], ['7', '101'],
         ['8', '0']]
test2 = [['000000000000000000000000000000X1001X'], ['42', '100'],
         ['00000000000000000000000000000000X0XX'], ['26', '1']]

assert current.part1(test1) == 165

assert current.part2(test2) == 208
