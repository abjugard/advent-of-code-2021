from santas_little_helpers import day, get_data, timed

today = day(2021, 4)


def calculate_score(last, drawn, card):
  unmarked = [n for row in card[:5] for n in row if n not in drawn]
  return last * sum(unmarked)


def has_bingo(drawn, card):
  return any(row <= drawn for row in card)


def bingo(draws, cards):
  star1_found = False
  for drawn, last in [(set(draws[0:i]), draws[i-1]) for i in range(5, len(draws))]:
    for idx, card in enumerate(cards):
      if has_bingo(drawn, card):
        if len(cards) == 1 or not star1_found:
          yield calculate_score(last, drawn, card)
          star1_found = True
        del cards[idx]


def parse_cards(raw_inp):
  for card_inp in raw_inp:
    candidates = [list(map(int, row.split())) for row in card_inp.split('\n')]
    candidates.extend(map(list, zip(*candidates)))
    yield [frozenset(candidate) for candidate in candidates]


def parse(raw_inp):
  draws = list(map(int, next(raw_inp).split(',')))
  cards = list(parse_cards(raw_inp))
  return draws, cards


def main():
  draws, cards = parse(get_data(today, [], groups=True))
  stars = bingo(draws, cards)
  print(f'{today} star 1 = {next(stars)}')
  print(f'{today} star 2 = {next(stars)}')


if __name__ == '__main__':
  timed(main)
