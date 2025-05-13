N = int(input())

# 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만듦
# 각 자리의 숫자를 더함
# 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 가장 오른쪽 자리 수를 이어붙임
# 원래 수로 돌아오는 사이클의 길이 구하기

ori = N
cnt = 0 
while True:
  a = N // 10
  b = N % 10
  c = (a + b) % 10
  N = b * 10 + c
  cnt += 1
  if N == ori:
    break

print(cnt)