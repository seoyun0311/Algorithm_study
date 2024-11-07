n = int(input())

dp = [-1 for _ in range(n)]

for idx in range(n):
    if idx < 3 :
        dp[idx] = idx+1
    else:
        dp[idx] = dp[idx-1] + dp[idx-2]

print(dp[-1]%10007)