from santas_little_helpers import day, get_data, timed
from itertools import product
from functools import cache

today = day(2021, 21)

dice_rolled = 0
dice_probabilities = list(zip(range(3, 10), [1, 3, 6, 7, 6, 3, 1]))


def roll():
  global dice_rolled
  dice_rolled += 1
  result = (dice_rolled % 100)
  return result


def practice_game(positions):
  scores = [0, 0]
  while all(score < 1000 for score in scores):
    for player in range(2):
      dice = sum([roll(), roll(), roll()])
      positions[player] = (positions[player] + dice) % 10
      scores[player] += positions[player] + 1
      if scores[player] >= 1000:
        break
  return min(scores) * dice_rolled


@cache
def play(positions, scores=(0, 0), turn=0):
  if scores[turn-1] >= 21:
    return [1, 0] if turn == 1 else [0, 1]
  wins = [0, 0]
  positions, scores = list(positions), list(scores)
  for dice, times in dice_probabilities:
    p, s = positions.copy(), scores.copy()
    p[turn] = (p[turn] + dice) % 10
    s[turn] += p[turn] + 1

    w = play(tuple(p), tuple(s), (turn + 1) % 2)
    wins[0] += w[0]*times
    wins[1] += w[1]*times
  return wins


def main():
  starting_positions = tuple(get_data(today, [('func', lambda s: int(s[-1])-1)]))
  print(f'{today} star 1 = {practice_game(list(starting_positions))}')
  print(f'{today} star 2 = {max(play(starting_positions))}')


if __name__ == '__main__':
  timed(main)
