from santas_little_helpers import day, get_data, timed
from santas_little_utils import tesseract_parse

today = day(2021, 13)


def reshape_x(paper, index):
  reshaped = set()
  for (x, y) in paper:
    n_x = x if x < index else index-(x-index)
    reshaped.add((n_x, y))
  return reshaped


def reshape_y(paper, index):
  reshaped = set()
  for (x, y) in paper:
    n_y = y if y < index else index-(y-index)
    reshaped.add((x, n_y))
  return reshaped


def reshape(paper, axis, index):
  if axis == 'x': return reshape_x(paper, index)
  if axis == 'y': return reshape_y(paper, index)


def fold(paper, instructions):
  star1 = None
  for axis, index in instructions:
    paper = reshape(paper, axis, int(index))
    if star1 is None:
      star1 = len(paper)
  return star1, paper


def read(paper):
  max_x = max(x for x, _ in paper)
  max_y = max(y for _, y in paper)
  result = []
  for y in range(max_y+1):
    result.append([])
    for x in range(max_x+1):
      result[y].append(1 if (x, y) in paper else 0)
  return ''.join(c for c in tesseract_parse(result) if c != ' ')


def parse(inp):
  points = set(tuple(map(int, point.split(','))) for point in next(inp).split())
  instructions = [l.split()[2].split('=') for l in next(inp).split('\n')]
  return points, instructions


def main():
  points, instructions = parse(get_data(today, [], groups=True))
  star1, paper = fold(points, instructions)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {read(paper)}')


if __name__ == '__main__':
  timed(main)
