N, M = map(int, input().split())
forest = list(map(int, input().split()))

s = 0
e = max(forest)

while s <= e:
  mid = (s+e)//2

  wood = 0
  for tree in forest:
    if tree >= mid:
      wood += tree - mid

  if wood >= M:
    s = mid + 1
  else:
    e = mid - 1

print(e)