from santas_little_helpers import day, get_data, timed
from itertools import product

today = day(2021, 17)


def step(vx, vy, x, y):
  x += vx
  y += vy
  if vx != 0:
    vx = vx + 1 if vx < 0 else vx - 1
  vy -= 1
  return vx, vy, x, y


def simulate(vx, vy, xs, ys):
  x, y, max_y = [0] * 3
  for _ in range(300):
    vx, vy, x, y = step(vx, vy, x, y)
    max_y = max(max_y, y)
    if x in xs and y in ys:
      return True, max_y
    if vy < 0 and y < min(ys):
      break
    if vx > 0 and x > max(xs):
      break
    if vx == 0 and x not in xs:
      break
  return False, None


def brute_force(target):
  count, max_y = [0] * 2
  for vx, vy in product(*[range(-200, 200)]*2):
    hits, y_reached = simulate(vx, vy, *target)
    if hits:
      max_y = max(max_y, y_reached)
    count += hits
  return max_y, count


def parse(inp):
  l, r = inp[13:].split(', ')

  def parse_range(s):
    axis, s = s.split('=')
    start, end = s.split('..')
    return axis, range(int(start), int(end) + 1)

  l_axis, lr = parse_range(l)
  _, rr = parse_range(r)

  if l_axis.lower() == 'x':
    return lr, rr
  return rr, lr


def main():
  target = parse(next(get_data(today)))
  star1, star2 = brute_force(target)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')


if __name__ == '__main__':
  timed(main)
