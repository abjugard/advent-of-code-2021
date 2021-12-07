from santas_little_helpers import day, get_data, timed
from sys import maxsize

today = day(2021, 7)


def optimise_crab_moves(positions):
  star1, star2 = [maxsize] * 2
  for target in range(min(positions), max(positions)):
    moves = [abs(target - n) for n in positions]
    star1 = min(star1, sum(moves))
    star2 = min(star2, sum((m * (m + 1)) // 2 for m in moves))

  return (star1, star2)


def main():
  inp = next(get_data(today, [('split', ','), ('map', int)]))
  star1, star2 = optimise_crab_moves(inp)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')


if __name__ == '__main__':
  timed(main)
