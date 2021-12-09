from santas_little_helpers import day, get_data, timed
from collections import Counter

today = day(2021, 9)

dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]


def neighbours(p):
  x, y = p
  for xd, yd in dirs:
    yield x + xd, y + yd


def discover_lows(c_map):
  for p in c_map.keys():
    neighs = [c_map[p_n] for p_n in neighbours(p) if p_n in c_map]
    if all(neigh > c_map[p] for neigh in neighs):
      yield 1 + c_map[p]


def find_low(c_map, p):
  ps = [p_n for p_n in neighbours(p) if p_n in c_map and c_map[p] > c_map[p_n]]
  return p if len(ps) == 0 else find_low(c_map, ps[0])


def find_largest_basins(c_map):
  basins = Counter(find_low(c_map, p) for p in c_map)
  basin_sizes = sorted(basins.values(), reverse=True)
  star2 = 1
  for size in basin_sizes[:3]:
    star2 *= size
  return star2


def build_map(cave):
  c_map = dict()
  for y, xs in enumerate(cave):
    c_map.update({(x, y): int(h) for x, h in enumerate(xs) if h != '9'})
  return c_map


def main():
  cave = list(get_data(today))
  c_map = build_map(cave)
  print(f'{today} star 1 = {sum(discover_lows(c_map))}')
  print(f'{today} star 2 = {find_largest_basins(c_map)}')

if __name__ == '__main__':
  timed(main)
