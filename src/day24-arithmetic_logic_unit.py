from santas_little_helpers import day, get_data, timed
from functools import cache

today = day(2021, 24)


def validate(inp):
  regs = {c: 0 for c in 'wxyz'}
  def parse_args(args):
    reg, val = args
    val = regs[val] if val in 'wxyz' else int(val)
    return reg, val
  for instr, *args in program:
    if instr == 'inp':
      regs[args[0]] = int(inp.pop(0))
      continue
    reg, val = parse_args(args)
    match instr:
      case 'add': regs[reg]  += val
      case 'mul': regs[reg]  *= val
      case 'div': regs[reg] //= val
      case 'mod': regs[reg]  %= val
      case 'eql': regs[reg]  &= val
  return regs['z'] == 0


@cache
def run_optimised(z, inp, z_div, x_add, y_add):
  x = x_add + z % 26
  z //= z_div
  if x != inp:
    z *= 26
    z += inp + y_add
  return z


@cache
def dfs(maximum, idx=0, z=0):
  if idx == 14:
    return z == 0, ''
  if z > z_max[idx]:
    return False, None
  cand = range(1, 10)
  for inp in reversed(cand) if maximum else cand:
    next_z = run_optimised(z, inp, *arg_sets[idx])
    found, s = dfs(maximum, idx + 1, next_z)
    if found:
      return True, str(inp) + s
  return False, None


def find_and_validate(maximum=True):
  result = dfs(maximum)[1]
  is_valid = validate(list(result))
  if not is_valid:
    print('result not valid')
    exit()
  return result


def setup(inp):
  global program, arg_sets, z_max
  program = list(inp)
  arg_sets, z_max, zdivs = [], [], []
  for i in range(14):
    offsets = [18*i+o for o in [4, 5, 15]]
    arg_set = tuple(int(program[offset][-1]) for offset in offsets)
    zdivs.append(arg_set[0])
    arg_sets.append(arg_set)
  for i in range(14):
    div_ops_left = len([1 for zdiv in zdivs[i:] if zdiv == 26])
    z_max.append(pow(23, div_ops_left))


def main():
  setup(get_data(today, [('split', ' ')]))
  print(f'{today} star 1 = {find_and_validate()}')
  print(f'{today} star 2 = {find_and_validate(maximum=False)}')


if __name__ == '__main__':
  timed(main)
