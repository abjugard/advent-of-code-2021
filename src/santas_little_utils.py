from collections import deque

directions_8 = [(-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                (-1,  1), (0,  1), (1,  1)]

directions_4 = [(0, -1), (-1, 0), (1, 0), (0, 1)]


def get_iterator(variable):
  try:
    it = iter(variable)
    return it
  except TypeError:
    return get_iterator([variable])


def get_last(generator):
  d = deque(generator, maxlen=2)
  d.pop()
  return d.pop()


def ellipse(y, x, px_width):
  yp = (y + 2) * px_width
  xp = (x + 2) * px_width
  return (xp, yp), (xp + px_width + 7, yp + px_width + 7)


def create_image(result):
  from PIL import Image, ImageDraw
  px_width = 8
  dimensions = ((len(result[0]) + 4) * px_width, (len(result) + 4) * px_width)
  img = Image.new('RGBA', dimensions, (255, 255, 255, 0))
  draw = ImageDraw.Draw(img)
  for y, xs in enumerate(result):
    for x, value in enumerate(xs):
      if value == 1:
        draw.ellipse(ellipse(y, x, px_width), fill='black')
  return img


def tesseract_parse(inp):
  try:
    import pytesseract
    image = inp
    if isinstance(inp, list):
      image = create_image(inp)
    return pytesseract.image_to_string(image, config='--psm 6')
  except ImportError:
    for line in inp:
      print(''.join('█' if c == 1 else ' ' for c in line))
    print('for cooler results, please install Pillow and pytesseract\n' \
        + '(along with a tesseract-ocr distribution)')
    return None


def build_dict_map(map_data):
  the_map = dict()
  for y, xs in enumerate(map_data):
    the_map.update({(x, y): int(h) for x, h in enumerate(xs)})
  return the_map


def build_grid(map_data):
  return [xs for xs in map_data]


def neighbours(p, borders=None, diagonals=True):
  def within_borders(p_n, borders):
    match borders:
      case None: return True
      case dict(): return p_n in borders
      case list():
        x_n, y_n = p_n
        h = len(borders)
        return h > 0 and 0 <= y_n < h and 0 <= x_n < len(borders[0])
      case _:
        print(type(borders))
        raise Exception('unknown datastructure')
  x, y = p
  for xd, yd in directions_8 if diagonals else directions_4:
    p_n = x + xd, y + yd
    if within_borders(p_n, borders):
      yield p_n
