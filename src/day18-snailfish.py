import json
from santas_little_helpers import day, get_data, timed
from math import ceil, floor

today = day(2021, 18)


def split(number):
  if isinstance(number, int):
    if number > 9:
      return True, [floor(number / 2), ceil(number / 2)]
    return False, number
  l, r = number
  action, l = split(l)
  if action:
    return True, [l, r]
  action, r = split(r)
  return action, [l, r]


def add_to_left(number, other):
  if isinstance(number, int):
    return number + other
  return [add_to_left(number[0], other), number[1]]


def add_to_right(number, other):
  if isinstance(number, int):
    return number + other
  return [number[0], add_to_right(number[1], other)]


def explode(number, depth=0):
  if isinstance(number, int):
    return False, number, 0, 0
  l, r = number
  if depth == 4:
    return True, 0, l, r
  action, l, l_inner, r_inner = explode(l, depth + 1)
  if action:
    return True, [l, add_to_left(r, r_inner)], l_inner, 0
  action, r, l_inner, r_inner = explode(r, depth + 1)
  if action:
    return True, [add_to_right(l, l_inner), r], 0, r_inner
  return False, number, 0, 0


def do_reduce(number):
  while True:
    action, number, *_ = explode(number)
    if action:
      continue
    action, number = split(number)
    if not action:
      break
  return number


def magnitude(number):
  if isinstance(number, int):
    return number
  return 3 * magnitude(number[0]) + 2 * magnitude(number[1])


def magnitude_of_sum(numbers):
  result, *rest = numbers
  for number in rest:
    result = do_reduce([result, number])
  return magnitude(result)


def max_magnitude_of_two(numbers):
  max_magnitude = 0
  for base in numbers:
    for other in [other for other in numbers if other != base]:
      max_magnitude = max(max_magnitude, magnitude(do_reduce([base, other])))
  return max_magnitude


def main():
  inp = list(get_data(today, [('func', json.loads)]))
  print(f'{today} star 1 = {magnitude_of_sum(inp)}')
  print(f'{today} star 2 = {max_magnitude_of_two(inp)}')


if __name__ == '__main__':
  timed(main)
