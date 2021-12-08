from santas_little_helpers import day, get_data, timed
from collections import Counter

today = day(2021, 8)


def obvious_outputs(data):
  counts = Counter(len(out) for outputs, _ in data for out in outputs)
  return sum(counts[l] for l in [2, 3, 4, 7])


def unscramble(output, four, one):
  match len(output):
    case 2: return '1'
    case 3: return '7'
    case 4: return '4'
    case 7: return '8'
    case 5:
      match len(output & four), len(output & one):
        case 2, _: return '2'
        case 3, 1: return '5'
        case 3, 2: return '3'
    case 6:
      match len(output & four), len(output & one):
        case 4, _: return '9'
        case 3, 1: return '6'
        case 3, 2: return '0'


def unscramble_outputs(outputs, patterns):
  return int(''.join(unscramble(output, *patterns) for output in outputs))


def unscramble_displays(data):
  return sum(unscramble_outputs(*pair) for pair in data)


def parse(line):
  patterns, outputs = line.split('|')
  patterns = {len(s): set(s) for s in patterns.split()}
  outputs = [set(s) for s in outputs.split()]
  return (outputs, (patterns[4], patterns[2]))


def main():
  data = list(get_data(today, [('func', parse)]))
  print(f'{today} star 1 = {obvious_outputs(data)}')
  print(f'{today} star 2 = {unscramble_displays(data)}')


if __name__ == '__main__':
  timed(main)
