from santas_little_helpers import day, get_data, timed

today = day(2021, 1)


def larger_than_previous(depths):
  return sum(right > left for left, right in zip(depths, depths[1:]))


def sliding_window(depths):
  increases = 0
  last = sum(depths[0:3])
  for i in range(1, len(depths) - 2):
    window = sum(depths[i:i+3])
    increases += window > last
    last = window
  return increases


def main():
  depths = list(get_data(today, [('func', int)]))
  print(f'{today} star 1 = {larger_than_previous(depths)}')
  print(f'{today} star 2 = {sliding_window(depths)}')


if __name__ == '__main__':
  timed(main)
