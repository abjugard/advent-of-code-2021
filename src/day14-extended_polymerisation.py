from santas_little_helpers import day, get_data, timed
from collections import Counter

today = day(2021, 14)


def score(template, pairs):
  counts = Counter()
  for (left, _), count in pairs.items():
    counts[left] += count
  counts[template[-1]] += 1

  counts = counts.most_common()
  return (counts[0][1] - counts[-1][1])


def expand(template, rules, checkpoints):
  pairs = Counter()
  for a, b in zip(template, template[1:]):
    pairs[(a, b)] += 1

  for t in range(max(checkpoints)):
    n_pairs = Counter()
    for (a, b), count in pairs.items():
      if (a, b) in rules:
        c = rules[(a, b)]
        n_pairs[(a, c)] += count
        n_pairs[(c, b)] += count
      else:
        n_pairs[(a, b)] += count
    pairs = n_pairs
    if t + 1 in checkpoints:
      yield score(template, pairs)


def parse(line):
  if not '>' in line:
    return line
  return tuple(line.split(' -> '))


def main():
  template, _, *rules = list(get_data(today, [('func', parse)]))
  rules = {tuple(p): c for p, c in rules}
  star_gen = expand(template, rules, [10, 40])
  print(f'{today} star 1 = {next(star_gen)}')
  print(f'{today} star 2 = {next(star_gen)}')


if __name__ == '__main__':
  timed(main)
