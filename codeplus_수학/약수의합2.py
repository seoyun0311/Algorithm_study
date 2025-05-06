def g(n):
  result = 0 
  for i in range(1, n+1):
    result += (n // i) * i
  return result

# 입력
N = int(input())
print(g(N))