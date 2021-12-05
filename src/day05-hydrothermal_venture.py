from santas_little_helpers import day, get_data, timed
from collections import Counter

today = day(2021, 5)


def straight_lines(all_lines):
  straights = [(l, r) for l, r in all_lines if l[0] == r[0] or l[1] == r[1]]
  counter = Counter()

  for (x1, y1), (x2, y2) in straights:
    x_s, y_s = min(x1, x2), min(y1, y2)
    x_e, y_e = max(x1, x2), max(y1, y2)

    for x in range(x_s, x_e + 1):
      for y in range(y_s, y_e + 1):
        counter[(x, y)] += 1

  return (sum(count > 1 for count in counter.values()), counter)


def diagonal_lines(all_lines, counter):
  diagonals = [(l, r) for l, r in all_lines if l[0] != r[0] and l[1] != r[1]]

  for (x, y), (x_end, y_end) in diagonals:
    x_step = -1 if x > x_end else 1
    y_step = -1 if y > y_end else 1

    counter[(x, y)] += 1
    while x != x_end:
      x += x_step
      y += y_step
      counter[(x, y)] += 1

  return sum(count > 1 for count in counter.values())


def parse(line):
  sides = line.split(' -> ')
  return tuple(tuple(map(int, side.split(','))) for side in sides)


def main():
  lines = list(get_data(today, [('func', parse)]))
  star1, counter = straight_lines(lines)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {diagonal_lines(lines, counter)}')


if __name__ == '__main__':
  timed(main)
