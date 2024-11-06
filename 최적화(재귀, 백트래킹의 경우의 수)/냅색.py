import sys
input = sys.stdin.readline

def recur(idx, W, V):
  global answer
  if W > B:
    return
  if idx == N:
    answer = max(answer, V)
    return

  #만약 배낭에 물건을 넣는다면
  recur(idx + 1, W + bag[idx][0], V + bag[idx][1])

  # 만약 배낭에 물건을 넣지 않는다면
  recur(idx+1, W, V)

N, B = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
answer = 0 
recur(0, 0, 0)

print(answer)