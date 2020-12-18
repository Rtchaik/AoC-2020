import Day18.solution as current

test1 = '1 + 2 * 3 + 4 * 5 + 6'
test2 = '1 + (2 * 3) + (4 * (5 + 6))'
test3 = '2 * 3 + (4 * 5)'
test4 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
test5 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
test6 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'

assert current.make_math(test1)[0] == 71
assert current.make_math(test2)[0] == 51
assert current.make_math(test3)[0] == 26
assert current.make_math(test4)[0] == 437
assert current.make_math(test5)[0] == 12240
assert current.make_math(test6)[0] == 13632

assert current.make_math(test1, False)[0] == 231
assert current.make_math(test2, False)[0] == 51
assert current.make_math(test3, False)[0] == 46
assert current.make_math(test4, False)[0] == 1445
assert current.make_math(test5, False)[0] == 669060
assert current.make_math(test6, False)[0] == 23340
