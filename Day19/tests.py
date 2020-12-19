import Day19.solution as current

test1 = ({
    '4': ['a'],
    '5': ['b'],
    '2': ['aa', 'bb'],
    '3': ['ab', 'ba'],
    '1': ['aaab', 'aaba', 'bbab', 'bbba', 'abaa', 'abbb', 'baaa', 'babb'],
    '0': [
        'aaaabb', 'aaabab', 'abbabb', 'abbbab', 'aabaab', 'aabbbb', 'abaaab',
        'ababbb'
    ]
}, ['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb'])

assert current.part1(test1) == 2
