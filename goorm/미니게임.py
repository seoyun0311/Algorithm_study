# 윳놀이 Y(2), 같은 그림 찾기 F(3), 원카드 O(4)
# 각각 2,3,4 명이서 플레이하는 게임
# 윳놀이 Y(1), 같은 그림 찾기 F(2), 원카드 O(3)
# 입력 : 플레이 횟수 N, 플레이할 게임의 종류
# 출력 : 최대 몇 번이나 게임을 플레이할 수 있는지
# 중복 x, 동명이인 x
import sys
input = sys.stdin.readline

N, G = input().split()
N = int(N)

played = set()

for i in range(N):
    play = input().strip()
    played.add(play)

if G == 'Y':
    print(len(played))
elif G == 'F':
    print(len(played)//2)
else:
    print(len(played)//3)
