from santas_little_helpers import day, get_data, timed
from santas_little_utils import build_dict_map, neighbours

today = day(2021, 11)


def visit(cave, flashed, p):
  cave[p] += 1
  if cave[p] > 9 and p not in flashed:
    flashed.add(p)
    for p_n in neighbours(p, cave):
      visit(cave, flashed, p_n)


def simulate_octopi(cave):
  count = step = 0
  while step := step + 1:
    flashed = set()
    for p in cave:
      visit(cave, flashed, p)
    count += len(flashed)
    if step == 100:
      yield count
    if len(flashed) == len(cave):
      yield step
    for p in flashed:
      cave[p] = 0


def main():
  cave = build_dict_map(get_data(today))
  star_gen = simulate_octopi(cave)
  print(f'{today} star 1 = {next(star_gen)}')
  print(f'{today} star 2 = {next(star_gen)}')


if __name__ == '__main__':
  timed(main)
