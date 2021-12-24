from santas_little_helpers import day, get_data, timed
from collections import defaultdict
from functools import cache

today = day(2021, 20)

nine_grid = [(-1, -1), (0, -1), (1, -1),
             (-1,  0), (0,  0), (1,  0),
             (-1,  1), (0,  1), (1,  1)]


@cache
def all_points(x, y):
  return [(x + xd, y + yd) for xd, yd in nine_grid]


@cache
def compute_index(vals):
  n = ['1' if val else '0' for val in vals]
  return int(''.join(n), 2)


def enhance(image, algo, next_default):
  active = set(p for p, v in image.items() if v)
  xs = [x for x, _ in active]
  ys = [y for _, y in active]
  min_x, max_x = min(xs), max(xs)
  min_y, max_y = min(ys), max(ys)
  next_image = defaultdict(lambda: next_default)
  for y in range(min_y - 1, max_y + 2):
    for x in range(min_x - 1, max_x + 2):
      idx = compute_index(tuple(image[p] for p in all_points(x, y)))
      next_image[(x, y)] = algo[idx]
  return next_image


def enhance_image(algo, image, checkpoints):
  next_default = algo[0]
  for t in range(1, max(checkpoints) + 1):
    image = enhance(image, algo, next_default)
    next_default = not next_default
    if t in checkpoints:
      yield len([c for _, c in image.items() if c])


def parse(inp):
  algo = [c == '#' for c in next(inp)]
  input_image = defaultdict(lambda: False)
  for y, xs in enumerate(next(inp).split('\n')):
    for x, c in enumerate(xs):
      input_image[(x, y)] = c == '#'
  return algo, input_image


def main():
  algo, input_image = parse(get_data(today, [], groups=True))
  star_gen = enhance_image(algo, input_image, [2, 50])
  print(f'{today} star 1 = {next(star_gen)}')
  print(f'{today} star 2 = {next(star_gen)}')


if __name__ == '__main__':
  timed(main)
