from santas_little_helpers import day, get_data, timed
from sys import maxsize

today = day(2021, 7)


def calculate_fuel(positions):
  target = sorted(positions)[len(positions) // 2]
  return sum(abs(target - pos) for pos in positions)


def cost(move):
  return (move * (move + 1)) // 2


def calculate_fuel_advanced(positions):
  target = sum(positions) // len(positions)
  return sum(cost(abs(target - pos)) for pos in positions)


def main():
  positions = next(get_data(today, [('split', ','), ('map', int)]))
  print(f'{today} star 1 = {calculate_fuel(positions)}')
  print(f'{today} star 2 = {calculate_fuel_advanced(positions)}')


if __name__ == '__main__':
  timed(main)
