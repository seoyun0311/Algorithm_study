import sys
input = sys.stdin.readline

def recur(idx, W):
  global answer
  if W > B:
    return -9999999
  if idx == N:
    return 0
  if dp[idx][W] != -1:
    return dp[idx][W]

  dp[idx][W] = max(recur(idx + 1, W + bag[idx][0] + bag[idx][1]), recur(idx+1, W))


  return dp[idx][W]
N, B = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(100_001)] for _ in range(N)]

# 무게가 14남았고 2번째 물건이다
#dp[14][2]
recur(0, 0)

print(dp)