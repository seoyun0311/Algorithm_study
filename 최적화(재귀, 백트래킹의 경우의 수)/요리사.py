import sys
input = sys.stdin.readline

N = int(input())
food = [list(map(int, input().split())) for _ in range(N)]

def recur(idx, sin, sun, use):
  global answer

  if idx == N: 
    if use > 0:
      answer = min(answer, abs(sin-sun))
    return

  recur(idx + 1, sin * food[idx][0], sun + food[idx][1], use+1)
  recur(idx + 1, sin, sun, use)

answer = 99999999
recur(0, 1, 0, 0)
print(answer)