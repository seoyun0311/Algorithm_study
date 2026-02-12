# 비공식적인 국가간 순위
# 입력 : 각각 얻은 금, 은, 동 메달 수
# 1. 금메달 수가 더 많은 나라
# 2. 금메달 수가 같으면 은메달 수가 더 많은 나라
# 3. 금, 은 메달 수가 모두 같으면 동메달 수가 더 많은 나라
# 4. 금,은,동 메달 수가 모두 같으면 등수는 같음
# 출력 : 등수 = 자신보다 더 잘한 나라 수 + 1

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medals = {} # country_id -> (godal, silver, bronze)

for _ in range(N):
    c, g, s, b = map(int, input().split())
    medals[c] = (g, s, b)

gk, sk, bk = medals[K]

better = 0
for c, (g, s, b) in medals.items():
    if c == K:
        continue
    if (g > gk) or (g == gk and s > sk) or (g == gk and s == sk and b > bk):
        better += 1

print(better + 1)
