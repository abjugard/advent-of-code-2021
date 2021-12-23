from santas_little_helpers import day, timed, aoc_root

today = day(2021, 23)

travel_cost = {
  'd': 1000,
  'c': 100,
  'b': 10,
  'a': 1
}


def move_cost(move):
  times = int(move[1:])
  return travel_cost[move[0]] * times


def parse_work(part):
  cost = 0
  with (aoc_root / 'misc' / f'day23-p{part}-byhand.txt').open() as f:
    lines = f.read().strip().split('\n')
    for line in lines:
      if not any(c in line for c in 'abcd'):
        continue
      cost += sum(move_cost(move) for move in line.split())
  return cost


def main():
  print(f'{today} star 1 = {parse_work(1)}')
  print(f'{today} star 2 = {parse_work(2)}')


if __name__ == '__main__':
  timed(main)
