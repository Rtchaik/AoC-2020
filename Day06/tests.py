import Day06.solution as current

test1 = [[{'b', 'c', 'a'}], [{'a'}, {'b'}, {'c'}], [{'b', 'a'}, {'c', 'a'}], [{'a'}, {'a'}, {'a'}, {'a'}], [{'b'}]]

assert current.part1(test1) == 11

assert current.part2(test1) == 6
