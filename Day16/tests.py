import Day16.solution as current

test1 = ({
    'class': {1, 2, 3, 5, 6, 7},
    'row':
    {6, 7, 8, 9, 10, 11, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44},
    'seat': {
        13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50
    }
}, [7, 1, 14], [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]])

test2 = ({
    'class': {0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},
    'row': {0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},
    'seat': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19}
}, [11, 12, 13], [[3, 9, 18], [15, 1, 5], [5, 14, 9]])

assert current.part1(test1) == 71
#
# assert current.part2(test2) == {0: {'row'}, 1: {'class'}, 2: {'seat'}}