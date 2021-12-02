from santas_little_helpers import day, get_data, timed
from enum import Enum

today = day(2021, 2)


def calculate_position(steps):
  depth, travel_distance = 0, 0
  for direction, distance in steps:
    if direction == 'forward':
      travel_distance += distance
    elif direction == 'up':
      depth -= distance
    elif direction == 'down':
      depth += distance
  return depth * travel_distance


def calculate_position_2(steps):
  depth, travel_distance, aim = 0, 0, 0
  for direction, distance in steps:
    if direction == 'forward':
      travel_distance += distance
      depth += aim * distance
    elif direction == 'up':
      aim -= distance
    elif direction == 'down':
      aim += distance
  return depth * travel_distance


def parse(inp):
  direction, distance = inp.split()
  return (direction, int(distance))


def main() -> None:
  inp = list(get_data(today, [('func', parse)]))
  print(f'{today} star 1 = {calculate_position(inp)}')
  print(f'{today} star 2 = {calculate_position_2(inp)}')


if __name__ == '__main__':
  timed(main)
