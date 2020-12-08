import Day05.solution as current

test1 = 'FBFBBFFRLR'
test2 = 'BFFFBBFRRR'
test3 = 'FFFBBBFRRR'
test4 = 'BBFFBBFRLL'

assert current.seat(test1) == 357
assert current.seat(test2) == 567
assert current.seat(test3) == 119
assert current.seat(test4) == 820