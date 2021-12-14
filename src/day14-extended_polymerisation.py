from santas_little_helpers import day, get_data, timed
from collections import Counter

today = day(2021, 14)


def part1(template, rules):
  for _ in range(10):
    s = template
    for i, p in reversed(list(enumerate(zip(template, template[1:])))):
      s = s[:i+1] + rules[p] + s[i+1:]
    template = s

  counts = Counter(template).most_common()
  return counts[0][1] - counts[-1][1]


def parse(line):
  if not '>' in line:
    return line
  return tuple(line.split(' -> '))


def main():
  template, _, *rules = list(get_data(today, [('func', parse)]))
  rules = {tuple(p): c for p, c in rules}
  print(f'{today} star 1 = {part1(template, rules)}')


if __name__ == '__main__':
  timed(main)
