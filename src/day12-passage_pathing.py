from santas_little_helpers import day, get_data, timed
from networkx import DiGraph

today = day(2021, 12)


def all_paths(curr='start', visited=set(), visited_twice=True):
  if curr == 'end':
    return 1

  count = 0
  for cave in G.neighbors(curr):
    visited_twice_nest = visited_twice

    if cave in small_caves and cave in visited:
      if visited_twice_nest:
        continue
      visited_twice_nest = True

    count += all_paths(cave, visited | {cave}, visited_twice_nest)
  return count


def construct_graph(pairs):
  global G, small_caves
  G = DiGraph()
  for l, r in [sorted(p, key=len, reverse=True) for p in pairs]:
    if l != 'end':
      G.add_edge(l, r)
    if l != 'start':
      G.add_edge(r, l)
  small_caves = set(n for n in G.nodes() if n == n.lower())


def main():
  inp = list(get_data(today, [('split', '-'), ('func', tuple)]))
  construct_graph(inp)
  print(f'{today} star 1 = {all_paths()}')
  print(f'{today} star 2 = {all_paths(visited_twice=False)}')


if __name__ == '__main__':
  timed(main)
