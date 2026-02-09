# 입력 : 돌 N개
N = int(input())
# 상근이와 창영이는 번갈아가면서 돌을 1개 또는 3개 가져옴
# 마지막에 돌을 가져가는 사람이 이김
# 출력 : 이기는 사람
win = [-1]*10001

win[1] = 1 #SK
win[2] = 0 #CY
win[3] = 1 #SK

for i in range(4, N+1):
    if win[i-1] == 1 or win[i-3] == 1:
        win[i] = 0
    else:
        win[i] = 1

if win[N] == 1:
    print('SK')
else:
    print("CY")

# n-1 or n-3이 이미 존재한다면 그 결과의 반대가 나오게 된다.
# 따라서 n-1이나 n-3의 결과를 반대로 저장해주면 된다.

