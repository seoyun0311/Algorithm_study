N, M, K = map(int, input().split()) # 미로 크기 (N), 참가자 수 (M), 게임 시간(K)

# N (미로 정보)
arr = [list(map(int, input().split())) for _ in range(N)] 

# M (참가자의 좌표)
# 0:빈칸, 양수:벽, 음수:참가자
for _ in range(M):
  i, j = map(lambda x:int(x)-1, input().split()) # 1-based -> 0-based
  arr[i][j] -= 1 # 참가자 마킹 (1명 = -1, 2명 = -2 ... 누적 가능)
# -11:비상구
ei, ej = map(lambda x:int(x)-1, input().split())
arr[ei][ej]=-11 

# 정사각형 찾는 함수
def find_square(arr):
  # [1] 비상구와 모든 사람간의 가장 짧은 가로 또는 세로 거리 구하기 => L
  mn = N
  for i in range(N):
    for j in range(N):
      if -11 < arr[i][j] < 0: # 사람인 경우
        mn = min(mn, max(abs(ei - i), abs(ej - j))) # 가장 먼 거리의 사람과 출구의 가로/세로 거리
  # [2] (0,0)부터 순회하면서 길이 L인 정사각형에 비상구와 사람있는지 체크 => 리턴 L+1
  for si in range(N-mn):
    for sj in range(N-mn): # 시작 위치 순회
      if si<=ei<=si+mn and sj<=ej<=sj+mn: # 비상구가 포함된 사각형!
        for i in range(si, si+mn+1):
          for j in range(sj, sj+mn+1):
            if -11<arr[i][j]<0: # 사람도 포함된다면
              return si, sj, mn+1 # 좌상단 좌표와 한 변 길이 반환

# 비상구 위치 찾는 함수            
def find_exit(arr):
  for i in range(N):
    for j in range(N):
      if arr[i][j]==-11:
        return i, j
# 회전하면 비상구 위치가 바뀌기 때문에 매번 위치를 다시 찾기 위해 사용

# 시뮬레이션 시작
# K턴 또는 모두 탈출까지 모든 사람의 이동거리 누적, 모두 탈출했으면 종료
ans = 0 # 총 이동 거리
cnt = M # 아직 탈출하지 않은 사람 수
for _ in range(K):
  # [1] 모든 참가지 (동시에) 한 칸 이동 (출구 최단거리 방향 상/하 우선)
  # 출구에 도착하면 즉시 탈출
  narr = [x[:] for x in arr]
  for i in range(N):
    for j in range(N):
      if -11 < arr[i][j] < 0: # 사람인 경우
        dist = abs(ei-i)+abs(ej-j) # 현재 거리
        # 맨해튼 거리 사용하여 출구까지의 거리 계산
        # 네방향(상하우선), 범위내, 벽아니고 <=0, 거리가 dist 보다 작으면
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)): # 상하좌우 순서대로
          ni, nj = i+di, j+dj
          if 0<=ni<N and 0<=nj<N and arr[ni][nj]<=0 and dist>(abs(ei-ni)+abs(ej-nj)): # 더 가까워지는 방향
            ans += arr[i][j] # 현재 인원수가 이동하는 것이니 이동거리에 누적 (음수니까 나중에 -붙여서 출력력)
            narr[i][j] -= arr[i][j] # 현재 위치에서 인원 제거
            if arr[ni][nj] == -11: # 비상구인 경우
              cnt += arr[i][j] # 탈출!
            else:
              narr[ni][nj] += arr[i][j] # 들어온 인원 추가
            break # 한 칸만 이동하므로 break
    # 모두 탈출했는지 확인인     
    arr = narr
    if cnt == 0:
      break

    # [2] 미로 회전(출구와 한 명 이상 참가자를 포함하는 가장 작은 정사각형)
    # 시계방향 90도 : 같은 크기 -> 좌상단행열, 내구도 =1
    si, sj, L = find_square(arr)
    narr = [x[:] for x in arr]

    for i in range(L):
      for j in range(L):
        narr[si+i][sj+j] = arr[si+L-1-j][si+i] # 90도 회전전
        if narr[si+i][sj+j] > 0: # 벽이면 회전시 1 감소
          narr[si+i][sj+j] -= 1
    arr = narr
    # 회전으로 달라졌으므로 => 비상구 위치 저장
    ei, ej = find_exit(arr)

print(-ans) # 이동 거리 출력력
print(ei+1, ej+1) # 1-based 좌표 출력