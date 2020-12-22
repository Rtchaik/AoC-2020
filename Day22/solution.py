from collections import deque
from itertools import islice
from copy import deepcopy


def solveDay(my_file):
    data = parse_data(my_file)
    print('Part 1: ', part1(deepcopy(data)))
    print('Part 2: ', part2(data))


def parse_data(my_file):
    with open(my_file) as f:
        return [deque(map(int, player.split()[2:])) for player in f.read().split('\n\n')]


def part1(data):
    return sum(game(data))


def part2(data):
    return sum(game(data, True))


def game(data, rec_mode=False):
    history = set()
    while data[0] and data[1]:
        card1 = data[0].popleft()
        card2 = data[1].popleft()
        if card1 <= len(data[0]) and card2 <= len(data[1]) and rec_mode:
            new_game = game([deque(islice(data[0], card1)), deque(islice(data[1], card2))])
            result = (winner := not bool(new_game[0])), (card1, card2) if not winner else (card2, card1)
        else:
            result = card1 < card2, sorted((card1, card2), reverse=True)
        data[result[0]].extend(result[1])
        state = tuple(sum(card * idx for idx, card in enumerate(reversed(player), 1)) for player in data)
        if state in history:
            return state[0], 0
        else:
            history.add(state)
    return state
