from santas_little_helpers import day, get_data, timed
from collections import Counter

today = day(2021, 6)


def simulate_lanternfish(fish, t=80):
  for _ in range(t):
    next_fish = Counter()
    for f, count in fish.items():
      if f == 0:
        next_fish[8] += count
        next_fish[6] += count
      else:
        next_fish[f - 1] += count
    fish = next_fish

  return sum(fish.values())


def main():
  fish_input = Counter(next(get_data(today, [('split', ','), ('map', int)])))
  print(f'{today} star 1 = {simulate_lanternfish(fish_input)}')
  print(f'{today} star 2 = {simulate_lanternfish(fish_input, 256)}')


if __name__ == '__main__':
  timed(main)
