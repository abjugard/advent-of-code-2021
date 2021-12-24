from santas_little_helpers import day, get_data, timed, submit_answer
from itertools import combinations, product

today = day(2021, 19)


def calc_orientation(result_neighbours, scanner_neighbours):
  offset = [None] * 3
  direction = [None] * 3
  rotation = [None] * 3

  for axis, rotation_axis in product(range(3), repeat=2):
    for direction_flip in [-1, 1]:
      offsets = set()
      for result_n, scanner_n in zip(result_neighbours, scanner_neighbours):
        offsets.add(result_n[axis] - scanner_n[rotation_axis] * direction_flip)

      if len(offsets) == 1:
        offset[axis] = offsets.pop()
        direction[axis] = direction_flip
        rotation[axis] = rotation_axis

  return offset, direction, rotation


def reorient(offset, direction, rotation, points):
  return [tuple(p[rotation[axis]] * direction[axis] + offset[axis] for axis in range(3)) for p in points]


def find_match(result_map, scanner_maps):
  for result_key in result_map.keys():
    for scanner, scanner_map in scanner_maps.items():
      for scanner_key in [key for key in scanner_map.keys() if key == result_key]:
        result_neighbours = result_map[scanner_key]
        scanner_neighbours = scanner_map[scanner_key]
        return scanner, result_neighbours, scanner_neighbours


def distance(p, o):
  return sum(abs(p[axis] - o[axis]) for axis in range(3))


def calc_neighbours(points):
  neighbours = {}
  for point in points:
    distances = {}
    for other in [o for o in points if o is not point]:
      distances[distance(point, other)] = other

    dist_a, dist_b = sorted(distances)[:2]
    a = distances[dist_a]
    b = distances[dist_b]

    key = (dist_a + dist_b) * distance(a, b)
    neighbours[key] = (point, a, b)
  return neighbours


def map_result(scanner_data):
  result = set(scanner_data.pop(0))
  scanner_maps = {d: calc_neighbours(d) for d in scanner_data}
  scanner_positions = []

  while scanner_maps:
    result_map = calc_neighbours(result)
    scanner, result_neighbours, scanner_neighbours = find_match(result_map, scanner_maps)

    del scanner_maps[scanner]

    orientation = calc_orientation(result_neighbours, scanner_neighbours)
    result.update(reorient(*orientation, scanner))

    scanner_pos, _, _ = orientation
    scanner_positions.append(scanner_pos)

  return len(result), scanner_positions


def largest_distance(scanner_positions):
  return max(distance(l, r) for l, r in combinations(scanner_positions, 2))


def parse(group):
  _, *lines = group.split('\n')
  beacons = []
  for line in lines:
    beacons.append(tuple(map(int, line.split(','))))
  return tuple(beacons)


def main():
  scanner_data = list(get_data(today, [('func', parse)], groups=True))
  star1, scanner_positions = map_result(scanner_data)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {largest_distance(scanner_positions)}')


if __name__ == '__main__':
  timed(main)
