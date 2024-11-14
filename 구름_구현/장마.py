import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
rain = set()
water = [0] * N

for i in range(1, M+1):
	si, ei = map(int, input().split())
	for j in range(si-1, ei):
		water[j] += 1
		rain.add(j)
		
	if i%3 == 0:
		for k in rain:
			water[k] -= 1
		rain.clear()
			
for i in range(N):
	arr[i] += water[i]

print(*arr)