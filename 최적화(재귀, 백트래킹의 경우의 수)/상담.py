import sys
input = sys.stdin.readline

def recur(idx, price):
  global answer

  if idx > N :
    answer = max(answer, price)
    return

  # 만약 상담을 받는다면
  if idx + interview[idx][0] <= N+1:
   recur(idx + interview[idx][0], price + interview[idx][1])
  # 만약 상담을 받지 않는다면
  recur(idx+1, price)

# 입력
N = int(input())
interview = [[]] + [list(map(int, input().split())) for _ in range(N)]

answer = 0
recur(1, 0)
print(answer)