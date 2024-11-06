# 입력 : 수열의 길이 N, 수열
N = int(input())
arr = list(map(int, input().split()))


prefix = [0 for _ in range(N+1)]

for i in range(N):
  prefix[i+1] = max(prefix[i] + arr[i], arr[i])

print(max(prefix))


# 연속된 몇개의 수를 선택하여 구할 수 있는 합

# 가장 큰 합

# 다이나믹 프로그래밍