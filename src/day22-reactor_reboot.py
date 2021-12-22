from santas_little_helpers import day, get_data, timed
from itertools import product
from collections import defaultdict

today = day(2021, 22)


def subrange(r, boundary=range(-50, 51)):
  start = min(max(boundary.start, r.start), boundary.stop)
  stop = max(min(boundary.stop, r.stop), boundary.start)
  return range(start, stop)


def initialize_reactor(instructions):
  state = defaultdict(lambda: False)
  for ranges, target_state in instructions:
    for p in product(*[subrange(r) for r in ranges]):
      state[p] = target_state
  return sum(v for p, v in state.items())


def intersection(cube, other):
  return [subrange(*axis) for axis in zip(cube, other)]


def volume(cube):
  xs, ys, zs = cube
  return len(xs) * len(ys) * len(zs)


def unique_volume(cube, remaining):
  result = volume(cube)

  intersections = []
  for other in remaining:
    common = intersection(cube, other)
    if volume(common) > 0:
      intersections.append(common)

  for idx, common in enumerate(intersections):
    result -= unique_volume(common, intersections[idx + 1:])
  return result


def reboot_reactor(instructions):
  result = 0
  for idx, (cube, on) in enumerate(instructions):
    if on:
      result += unique_volume(cube, [other for other, _ in instructions[idx + 1:]])
  return result


def parse_axis(data):
  _, data = data.split('=')
  start, end = data.split('..')
  return range(int(start), int(end) + 1)


def parse(line):
  target_state, rest = line.split(' ')
  target_state = target_state == 'on'
  axis = [parse_axis(data) for data in rest.split(',')]
  return axis, target_state


def main():
  inp = list(get_data(today, [('func', parse)]))
  print(f'{today} star 1 = {initialize_reactor(inp)}')
  print(f'{today} star 2 = {reboot_reactor(inp)}')


if __name__ == '__main__':
  timed(main)
