# 점수는 내림차순, 같은 값 허용
# 같은 점수면 가장 높은 등수
# 리스트 최대 크기 P
# 리스트가 꽉 찼을 때
# 새 점수가 마지막 점수보다 작거나 같으면 -1
# 더 크면 들어갈 수 있음

# 1. N이 0 인경우 -> 아무도 없음 -> 무조건 1등
# 2. 새점수가 마지막 점수보다 작거나 같다면 -> 들어갈 수 없음 -> -1
# 3. 그외 -> 새 점수보다 큰 점수 개수 + 1 이 등수
import sys
input = sys.stdin.readline

N, new_score, P = map(int, input().split())
if N > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

# 1. N이 0 인 경우
if N == 0:
    print(1)
    exit()
# 2. 랭킹이 꽉찼고 새 점수가 마지막 점수보다 작거나 같다면
if N == P and new_score <= scores[-1]:
    print(-1)
    exit()
# 3. 등수 계산
rank = 1
for score in scores:
    if score > new_score:
        rank += 1
    else:
        break
print(rank)
