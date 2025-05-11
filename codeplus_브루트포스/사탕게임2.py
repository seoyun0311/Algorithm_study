N = int(input())
board = [list(input().strip()) for _ in range(N)]

# 사탕의 최대 개수 구하는 함수
# 오른쪽과 아래쪽만 검사하면 됨

def check(board, N):
  max_cnt = 1
  # 행 검사
  for i in range(N):
    cnt = 1
    for j in range(1, N):
      if board[i][j] == board[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      max_cnt = max(cnt, max_cnt)

  # 열 검사
  for j in range(N):
    cnt = 1
    for i in range(1,N):
      if board[i][j] == board[i-1][j]:
        cnt += 1
      else:
        cnt = 1
      max_cnt = max(cnt, max_cnt)
  return max_cnt

result = 0

# 먹을 수 있는 사탕의 최대 개수
for i in range(N):
  for j in range(N):
    # 오른쪽 교환
    if j + 1 < N and board[i][j] != board[i][j+1]:
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # swap
      result = max(result, check(board,N)) # 업데이트
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 복구

    # 아래쪽 교환
    if i + 1 < N and board[i][j] != board[i+1][j]:
      board[i][j], board[i+1][j] = board [i+1][j], board[i][j] # swap
      result = max(result, check(board,N)) # 업데이트
      board[i][j], board[i+1][j] = board [i+1][j], board[i][j] # 복구

print(result)