from santas_little_helpers import day, get_data, timed

today = day(2021, 8)


def easy_digits(data):
  outputs = [output for _, outputs in data for output in outputs]
  usable_outputs = [output for output in outputs if can_deduce_segments(output)]
  return len(usable_outputs)


def build(w, s):
  return ''.join(sorted(w[c] for c in s))


def parse_wires(signal_patterns, mapped):
  # wire 'a' is the only extra wire used for 7 in relation to 1
  wires = {'a': next(c for c in mapped[7] if c not in mapped[1])}

  # 0, 6 and 9 all use 6 wires
  sixs = [s for s in signal_patterns if len(s) == 6]

  # 6 is the only one that doesn't contain both of 'cf'
  mapped[6] = next(s for s in sixs if any(c not in s for c in mapped[1]))

  # 0 and 9 remain
  sixs = [s for s in sixs if s != mapped[6]]

  # find 'f' from 6, it's the only common wire with 1
  wires['f'] = next(c for c in mapped[6] if c in mapped[1])

  # 'c' is the other wire in 1
  wires['c'] = next(c for c in mapped[1] if c != wires['f'])

  # of 0 and 9, only 9 entirely contains 4
  mapped[9] = next(s for s in sixs if all(c in s for c in mapped[4]))

  # 'e' is the only unused wire in 9
  wires['e'] = next(c for c in 'abcdefg' if c not in mapped[9])

  # that leaves 0 from our six:s
  mapped[0] = next(s for s in sixs if s != mapped[9])

  # 'd' is the only wire in 4 not used in 0
  wires['d'] = next(c for c in mapped[4] if c not in mapped[0])

  # 'b' is the last wire in 4 we haven't yet mapped
  wires['b'] = next(c for c in mapped[4] if c not in build(wires, 'cdf'))

  # 'g' is the last wire we haven't yet mapped
  wires['g'] = next(c for c in mapped[8] if c not in ''.join(wires.values()))

  # fill in the blanks
  mapped[2] = build(wires, 'acdeg')
  mapped[3] = build(wires, 'acdfg')
  mapped[5] = build(wires, 'abdfg')


def construct_map(signal_patterns):
  decodable = [segment for segment in signal_patterns if can_deduce_segments(segment)]
  one, seven, four, eight = sorted(decodable, key=lambda s: len(s))
  mapped = {1: one, 4: four, 7: seven, 8: eight}
  parse_wires(signal_patterns, mapped)
  return {v: str(k) for k, v in mapped.items()}


def can_deduce_segments(segment):
  match len(segment):
    case 2 | 3 | 4 | 7:
      return True
    case _:
      return False


def decode_number(signal_patterns, outputs):
  the_map = construct_map(signal_patterns)
  return int(''.join([the_map[output] for output in outputs]))


def decode_numbers(data):
  results = [decode_number(*pair) for pair in data]
  return sum(results)


def parse(line):
  signal_patterns, outputs = line.split('|')
  signal_patterns = signal_patterns.split()
  outputs = outputs.split()
  return ([''.join(sorted(s)) for s in signal_patterns], [''.join(sorted(s)) for s in outputs])


def main():
  data = list(get_data(today, [('func', parse)]))
  print(f'{today} star 1 = {easy_digits(data)}')
  print(f'{today} star 2 = {decode_numbers(data)}')


if __name__ == '__main__':
  timed(main)
