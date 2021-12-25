from santas_little_helpers import day, get_data, timed

today = day(2021, 25)


def simulate_cucumbers(floor_map):
  h, w = len(floor_map), len(floor_map[0])
  steps = 0

  while True:
    total = 0

    moves = []
    vertical = []
    for y, xs in enumerate(floor_map):
      for x, c in enumerate(xs):
        if c == '>':
          if floor_map[y][(x + 1) % w] == '.':
            moves.append((x, y))
        elif c == 'v':
          vertical.append((x, y))
    total += len(moves)

    for x, y in moves:
      floor_map[y][x] = '.'
      floor_map[y][(x + 1) % w] = '>'

    moves = []
    for x, y in vertical:
      if floor_map[(y + 1) % h][x] == '.':
        moves.append((x, y))
    total += len(moves)

    for x, y in moves:
      floor_map[y][x] = '.'
      floor_map[(y + 1) % h][x] = 'v'

    steps += 1
    if total == 0:
      return steps


def main():
  floor_map = list(get_data(today, [('func', list)]))
  print(f'{today} star 1 = {simulate_cucumbers(floor_map)}')


if __name__ == '__main__':
  timed(main)
