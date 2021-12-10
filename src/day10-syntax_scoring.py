from santas_little_helpers import day, get_data, timed

today = day(2021, 10)

points = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
  '(': 1,
  '[': 2,
  '{': 3,
  '<': 4
}

opening = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}


def validate(line):
  stack = []
  for c in line:
    if c in opening:
      stack.append(c)
    else:
      if c != opening[stack.pop()]:
        return points[c], None
  return 0, stack


def syntax_error_score(navigation_program):
  results = [validate(line) for line in navigation_program]
  incomplete = [stack for score, stack in results if score == 0]
  return sum(score for score, _ in results), incomplete


def autocomplete_score(stack):
  score = 0
  for c in reversed(stack):
    score *= 5
    score += points[c]
  return score


def autocomplete(incomplete):
  results = sorted(autocomplete_score(stack) for stack in incomplete)
  return results[len(results) // 2]


def main():
  navigation_program = list(get_data(today))
  star1, incomplete = syntax_error_score(navigation_program)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {autocomplete(incomplete)}')


if __name__ == '__main__':
  timed(main)
