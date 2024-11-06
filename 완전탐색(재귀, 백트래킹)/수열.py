import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

def recur(number, start):
  if number == M:
    print(*arr)
    return
  
  for i in range(start, N+1):
    if i in arr:
      continue
    arr.append(i)
    recur(number + 1, i+1)
    arr.pop()

recur(0, 1)