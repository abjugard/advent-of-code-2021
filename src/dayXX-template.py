from santas_little_helpers import day, get_data, timed, submit_answer
from itertools import combinations

today = day(2021, ?)


def part1(ns):
  for n in ns:
    print(n)
  return 1


def part2(ns):
  for n in ns:
    print(n)
  return 2


def main():
  inp = list(get_data(today, [('func', int)]))
  star1 = part1(inp)
  # submit_answer(today, star1)
  print(f'{today} star 1 = {star1}')

  # star2 = part2(inp)
  # print(f'{today} star 2 = {star2}')
  # submit_answer(today, star2, 2)


if __name__ == '__main__':
  timed(main)
