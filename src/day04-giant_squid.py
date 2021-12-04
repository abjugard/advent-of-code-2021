from santas_little_helpers import day, get_data, timed

today = day(2021, 4)


def calculate_score(drawn, card):
  unmarked = [n for row in card[:5] for n in row if n not in drawn]
  return drawn[-1] * sum(unmarked)


def has_bingo(drawn, card):
  return any(all(n in drawn for n in row) for row in card)


def bingo(draws, cards):
  star1_found = False
  for drawn in [draws[0:i] for i in range(5, len(draws))]:
    for idx, card in enumerate(cards):
      if has_bingo(drawn, card):
        if len(cards) == 1 or not star1_found:
          yield calculate_score(drawn, card)
          star1_found = True
        del cards[idx]


def parse_cards(raw_inp):
  card = None
  for line in raw_inp:
    if line == '':
      if card is not None:
        card.extend(map(list, zip(*card)))
        yield card
      card = []
      continue
    nums = line.strip().split()
    card.append(list(map(int, nums)))
  yield card


def parse(raw_inp):
  draws = list(map(int, next(raw_inp).split(',')))
  cards = list(parse_cards(raw_inp))
  return draws, cards


def main() -> None:
  draws, cards = parse(get_data(today))
  stars = bingo(draws, cards)
  print(f'{today} star 1 = {next(stars)}')
  print(f'{today} star 2 = {next(stars)}')


if __name__ == '__main__':
  timed(main)
