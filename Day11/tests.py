import Day11.solution as current

test1 = [
    'L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL',
    'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL'
]

assert current.part1(test1) == 37

assert current.part2(test1) == 26
