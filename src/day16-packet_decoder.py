from santas_little_helpers import day, get_data, timed
from santas_little_utils import mul

today = day(2021, 16)


class Transmission:
  version_sum = 0
  packets = []

  def __init__(self, bits):
    self.bits = bits
    self.packets = self._parse()

  def _parse(self, total_packets=None):
    packets = []
    while '1' in self.bits:
      packets.append(self._read_next_packet())
      if total_packets is not None and len(packets) == total_packets:
        break
    return packets

  def _read_next_packet(self):
    t = self._read_header()
    data = self._read_literal() if t == 4 else self._read_operator()
    return t, data

  def _read(self, n, convert=True):
    data, self.bits = self.bits[:n], self.bits[n:]
    return int(data, 2) if convert else data

  def _read_header(self):
    self.version_sum += self._read(3)
    type_id = self._read(3)
    return type_id

  def _read_literal(self):
    number = ''
    while True:
      indicator = self._read(1)
      number += self._read(4, convert=False)
      if indicator == 0:
        break
    return int(number, 2)

  def _read_operator(self):
    length_type_id = self._read(1)
    match length_type_id:
      case 0:
        sub_length = self._read(15)
        sub_bits = self._read(sub_length, convert=False)
        sub_transmission = Transmission(sub_bits)
        packets = sub_transmission.packets
        self.version_sum += sub_transmission.version_sum
      case 1:
        n_packets = self._read(11)
        packets = self._parse(n_packets)
    return packets


ops = [sum, mul, min, max]


def decode(type_id, data):
  if type_id < 4:
    return ops[type_id](decode(*p) for p in data)
  elif type_id == 4:
    return data
  left, right, *_ = [decode(*p) for p in data]
  match type_id:
    case 5: return left > right
    case 6: return left < right
    case 7: return left == right


def main():
  inp = next(get_data(today))
  data = ''.join(bin(int(c, 16))[2:].zfill(4) for c in inp)
  bits = Transmission(data)
  print(f'{today} star 1 = {bits.version_sum}')
  print(f'{today} star 2 = {decode(*bits.packets[0])}')


if __name__ == '__main__':
  timed(main)
