import math 

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for x in A:
    if x > B:
        x = x - B
        cnt += math.ceil(x/C) + 1
    else:
        cnt += 1

print(cnt)