N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N)]

for idx in range(N)[::-1]:
  if idx + table[idx][0] > N:
    dp[idx] = dp[idx+1]
  else:
    dp[idx][W] = max(dp[idx + 1][W + bag[idx][0]] + bag[idx][1], dp[idx+1][W])


print(dp[0])