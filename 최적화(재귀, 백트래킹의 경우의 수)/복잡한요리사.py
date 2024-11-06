import sys
input = sys.stdin.readline

def recur(idx, A, B, C, D, E):
  global answer
  global used
  global answer_used

  if a <= A and b <= B and c <= C and d <= D:
    if answer > E:
      answer = min(answer, E)
      answer_used = []
      for i in used:
        answer_used.append(i)
  if idx == N:
    return
  
  used.append(idx+1)
# 재료를 사용한 경우에는 영양소가 더해짐
  recur(idx + 1, A+ingre[idx][0], B+ingre[idx][1], C+ingre[idx][2], D+ingre[idx][3], E+ingre[idx][4])
  used.pop()
# 재료를 사용하지 않은 경우에는 그냥 다음 재료로 넘어간다
  recur(idx + 1, A, B, C, D, E)


N = int(input())
a, b, c, d = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 99999999999
used = []
answer_used= []

recur(0, 0, 0, 0, 0, 0)

answer_used.sort()

if answer_used:
  print(answer)
  print(*answer_used)
else:
  print(-1)
