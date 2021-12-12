from santas_little_helpers import day, get_data, timed
import networkx as nx

today = day(2021, 12)


def all_paths(G, path=['start'], visited_twice=True):
  curr = path[-1]
  if curr == 'end':
    yield path

  for cave in G.neighbors(curr):
    visited_twice_nest = visited_twice

    if cave in small_caves and cave in path:
      if visited_twice_nest or cave in ('start', 'end'):
        continue
      visited_twice_nest = True

    for p_nest in all_paths(G, path + [cave], visited_twice_nest):
      yield p_nest


def construct_graph(pairs):
  global small_caves
  G = nx.Graph()
  small_caves = set(n for pair in pairs for n in pair if n == n.lower())
  G.add_edges_from(pairs)
  return G


def main():
  inp = list(get_data(today, [('split', '-'), ('func', tuple)]))
  G = construct_graph(inp)
  print(f'{today} star 1 = {len(list(all_paths(G)))}')
  print(f'{today} star 2 = {len(list(all_paths(G, visited_twice=False)))}')


if __name__ == '__main__':
  timed(main)
