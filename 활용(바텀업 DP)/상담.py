import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split()))]

dp = [[0]*(k+1) for _ in range(n+1)]

for idx in range(1, n+1):
  for weight in range(1, k+1):
    if weight < k:
      dp[idx][weight] = dp[idx-1][weight]
    else:
      dp[idx][weight] = max(dp[idx-1][weight-items[idx][0]] + items[idx][1], dp[idx-1][weight])

print(dp[n][k])