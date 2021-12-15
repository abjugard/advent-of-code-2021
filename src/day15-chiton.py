from santas_little_helpers import day, get_data, timed
from santas_little_utils import neighbours
import networkx as nx

today = day(2021, 15)


def build_graph(cave, mult=1):
  g = nx.DiGraph()
  w, h = len(cave[0]), len(cave)

  c = dict()
  for x in range(w * mult):
    for y in range(h * mult):
      c[x, y] = ((cave[y % h][x % w] - 1 + (x // w) + (y // h)) % 9) + 1
  for p in c:
    g.add_weighted_edges_from((p, n_p, c[n_p]) for n_p in neighbours(p, c, diagonals=False))
  return g, c


def determine_risk(cave, mult=1):
  g, c = build_graph(cave, mult)
  path = nx.astar_path(g, (0, 0), max(c))
  return sum(c[p] for p in path) - c[(0, 0)]


def main():
  cave = list(get_data(today, [('map', int)]))
  print(f'{today} star 1 = {determine_risk(cave)}')
  print(f'{today} star 2 = {determine_risk(cave, mult=5)}')


if __name__ == '__main__':
  timed(main)
