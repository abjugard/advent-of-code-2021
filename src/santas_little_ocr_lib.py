def __ellipse(y, x, px_width):
  yp = (y + 2) * px_width
  xp = (x + 2) * px_width
  return (xp, yp), (xp + px_width + 7, yp + px_width + 7)


def create_image(data, w, h):
  from PIL import Image, ImageDraw
  px_width = 16
  dimensions = ((w + 5) * px_width, (h + 5) * px_width)
  img = Image.new('RGBA', dimensions, (255, 255, 255, 0))
  draw = ImageDraw.Draw(img)
  for x, y in data:
    draw.ellipse(__ellipse(y, x, px_width), fill='black')
  return img


def __prepare_set(s):
  max_x = max(x for x, _ in s)
  max_y = max(y for _, y in s)
  return s, (max_x, max_y)


def __prepare_dict(d):
  keys = [key for key, value in d.items() if value]
  max_x = max(x for x, _ in keys)
  max_y = max(y for _, y in keys)
  return keys, (max_x, max_y)


def __prepare_grid(g):
  s = set()
  for y, xs in enumerate(g):
    for x in [x for x, c in enumerate(xs) if c]:
      s.append((x, y))
  return s


def set_to_grid(s, max_x, max_y):
  result = []
  for y in range(max_y + 1):
    l = []
    for x in range(max_x + 1):
      l.append((x, y) in s)
    result.append(l)
  return result


def parse_datastructure(inp):
  if isinstance(inp, set):
    data, boundary = __prepare_set(inp)
  elif isinstance(inp, dict):
    data, boundary = __prepare_dict(inp)
  elif isinstance(inp, list):
    max_y = len(inp)
    if max_y == 0:
      raise Exception('unusable grid')
    max_x = len(inp[0])
    if max_x == 0 or any(len(l) != len(inp[0]) for l in inp):
      raise Exception('unusable grid')
    boundary = (max_x, max_y)
    data = __prepare_grid(inp)
  return data, boundary
