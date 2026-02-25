import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

L = 1
R = M
ans = 0

for _ in range(J):
    x = int(input())
    if x < L:
        move = L - x
        ans += move
        L -= move
        R -= move
    elif x > R:
        move = x - R
        ans += move
        L += move
        R += move
    # else: 이미 바구니 범위 안이라 이동 없음

print(ans)
