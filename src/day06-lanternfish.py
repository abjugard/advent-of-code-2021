from santas_little_helpers import day, get_data, timed
from collections import Counter

today = day(2021, 6)


def simulate_lanternfish(fish, checkpoint):
  for t in range(max(checkpoint)):
    count = fish.pop(0)
    fish[6] += count
    fish.append(count)
    if t + 1 in checkpoint:
      yield sum(fish)


def main():
  fish_input = Counter(next(get_data(today, [('split', ','), ('map', int)])))
  state = [fish_input[age] for age in range(9)]
  stars = simulate_lanternfish(state, [80, 256])
  print(f'{today} star 1 = {next(stars)}')
  print(f'{today} star 2 = {next(stars)}')


if __name__ == '__main__':
  timed(main)
