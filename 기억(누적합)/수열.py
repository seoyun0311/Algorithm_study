# 입력 : 수열의 길이 A, 간격 B, 수열
# 주어진 간격만큼의 합을 구함
# 출력 : 가장 큰 수

# 입력
A, B = map(int,input().split())
arr = list(map(int, input().split()))

# 누적합 -> prefix
prefix = [0 for _ in range(A+1)]

for i in range(A):
  prefix[i+1] = prefix[i] + arr[i]

answer = []
for k in range(B, A+1):
  answer.append(prefix[k] - prefix[k-B])

print(max(answer))