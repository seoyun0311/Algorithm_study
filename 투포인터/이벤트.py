N, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))

cnt = 0
s = 0
e = N-1
remain = 0

while s <= e : # s와 e가 교차되면 멈춘다 
  if arr[e] >= X: # 최대 용량보다 크거나 같다면
    cnt += 1
    e -= 1
    continue
  
  if s == e: # 투포인터가 만나면 
    remain += 1 # 짜투리를 하나 추가 한다

  if arr[s] + arr[e] >= X/2: # 두 개의 남은 용량을 합쳐서 X/2이상이라면
    cnt += 1
    s += 1
    e -= 1

  else: # 조건에 맞지 않다면
    s += 1 # 수가 커진다
    remain += 1 # 짜투리를 하나 추가한다

print(cnt + remain/3)
