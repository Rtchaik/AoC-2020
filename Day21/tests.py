import Day21.solution as current

test1 = ([{'kfcds', 'mxmxvkd', 'nhms', 'sqjhc'},
          {'sbzzf', 'mxmxvkd', 'trh', 'fvjkl'}, {'fvjkl', 'sqjhc'},
          {'sbzzf', 'mxmxvkd', 'sqjhc'}], {
              'dairy': 'mxmxvkd',
              'fish': 'sqjhc',
              'soy': 'fvjkl'
          })

assert current.part1(test1) == 5

assert current.part2(test1) == 'mxmxvkd,sqjhc,fvjkl'
