from santas_little_helpers import day, get_data, timed

today = day(2021, 2)

FORWARD = 0
UP = 1
DOWN = 2


def calculate_position(steps):
  depth, travel_distance = 0, 0
  for direction, distance in steps:
    if direction is FORWARD:
      travel_distance += distance
    elif direction is UP:
      depth -= distance
    elif direction is DOWN:
      depth += distance
  return depth * travel_distance


def calculate_position_2(steps):
  depth, travel_distance, aim = 0, 0, 0
  for direction, distance in steps:
    if direction is FORWARD:
      travel_distance += distance
      depth += aim * distance
    elif direction is UP:
      aim -= distance
    elif direction is DOWN:
      aim += distance
  return depth * travel_distance


def parse_direction(direction):
  match direction:
    case 'u':
      return UP
    case 'd':
      return DOWN
  return FORWARD


def parse(step):
  direction, distance = step.split()
  return (parse_direction(direction[0]), int(distance))


def main() -> None:
  steps = list(get_data(today, [('func', parse)]))
  print(f'{today} star 1 = {calculate_position(steps)}')
  print(f'{today} star 2 = {calculate_position_2(steps)}')


if __name__ == '__main__':
  timed(main)
