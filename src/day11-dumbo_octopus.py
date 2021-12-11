from santas_little_helpers import day, get_data, timed

today = day(2021, 11)

dirs = [(-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0), 
        (-1,  1), (0,  1), (1,  1)]


def neighbours(p):
  x, y = p
  for xd, yd in dirs:
    yield x + xd, y + yd


def visit(cave, flashed, p):
  cave[p] += 1
  if cave[p] > 9 and p not in flashed:
    flashed.add(p)
    for p_n in [p_n for p_n in neighbours(p) if p_n in cave]:
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


def build_map(inp):
  cave = dict()
  for y, xs in enumerate(inp):
    cave.update({(x, y): int(h) for x, h in enumerate(xs)})
  return cave


def main():
  cave = build_map(get_data(today))
  star_gen = simulate_octopi(cave)
  print(f'{today} star 1 = {next(star_gen)}')
  print(f'{today} star 2 = {next(star_gen)}')


if __name__ == '__main__':
  timed(main)
