from santas_little_helpers import day, get_data, timed

today = day(2021, 3)


def bit_value_order(diag_data, offset):
  ones = sum(1 for entry in diag_data if entry[offset] == '1')
  return ('1', '0') if ones >= len(diag_data) / 2 else ('0', '1')


def get_power_consumption(diag_data):
  gamma_rate, epsilon_rate = '', ''
  for bit_pos in range(len(diag_data[0])):
    gamma_next, epsilon_next = bit_value_order(diag_data, bit_pos)
    gamma_rate += gamma_next
    epsilon_rate += epsilon_next
  return int(gamma_rate, 2) * int(epsilon_rate, 2)


def find_entry(diag_data, most_common=True, offset=0):
  mc, lc = bit_value_order(diag_data, offset)
  comp = mc if most_common else lc
  filtered_data = [entry for entry in diag_data if entry[offset] == comp]
  if len(filtered_data) == 1:
    return int(filtered_data[0], 2)
  return find_entry(filtered_data, most_common, offset + 1)


def get_life_support_rating(diag_data):
  oxygen_rating = find_entry(diag_data)
  co2_rating = find_entry(diag_data, False)
  return oxygen_rating * co2_rating


def main() -> None:
  diag_data = list(get_data(today))
  print(f'{today} star 1 = {get_power_consumption(diag_data)}')
  print(f'{today} star 2 = {get_life_support_rating(diag_data)}')


if __name__ == '__main__':
  timed(main)
