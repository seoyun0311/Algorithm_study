E, S, M = map(int, input().split())

year = 1
while True:
  e = (year - 1) % 15 + 1
  s = (year - 1) % 28 + 1
  m = (year - 1) % 19 + 1

  if e == E and s == S and m == M :
    print(year)
    break

  year += 1