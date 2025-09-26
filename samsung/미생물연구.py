from collections import deque

# 3. 시작 칸과 같은 번호로 4방향 연결된 하나의 군집을 모아 [아이디, 좌표들...]을 만들어 돌려줌
def bfs(v, si, sj):
    q = deque() # BFS용 큐(FIFO), popleft()로 앞에서 꺼냄
    sn = arr[si][sj]    # 시작 칸의 '미생물 번호'(아이디), 같은 번호끼리 한 군집

    rlst = []   # 반환 리스트: [아이디, [r,c], [r,c], ...] 형식

    q.append((si,sj))   # BFS 시작점 큐에 넣기
    v[si][sj]=sn    # 방문표시(0->미방문, 0이 아니면 방문), 편하게 '아이디'로 찍음
    rlst.append(sn) # rlst[0]에 아이디 저장
    rlst.append([si,sj])    # 시작 좌표 저장

    while q:    # 큐가 빌 때까지 반복
        ci, cj = q.popleft()   # 가장 먼저 들어온 좌표(가장 가까운 칸)부터 꺼냄
        # 4방향으로 같은 아이디가 이어지면 같은 군집
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)): # 위, 아래, 왼, 오른
            ni, nj = ci+di, cj+dj   # 이웃 좌표
            # 격자 안, 미방문, 같은 sn(아이디)면 큐에 추가
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==sn:
                q.append((ni,nj))   # 다음에 탐색하도록 큐에 넣고
                v[ni][nj]=sn    # 즉시 방문표시(중복 enqueue 방지)
                rlst.append([ni,nj])    # 군집 좌표 목록에 추가
    return rlst # [아이디, 좌표들...] 반환

# 2. 격자 전체를 돌면서 군집들을 전부 뽑아 glst에 쌓음
def group():
    v = [[0] * N for _ in range(N)] # 방문배열(전체 BFS에서 공유)
    glst = []   # 모든 군집 목록

    for si in range(N):
        for sj in range(N):
            # 아직 안 갔고, 미생물이 있는 칸이면 새 군집 시작
            if v[si][sj]==0 and arr[si][sj]>0: # arr[si][sj]>0이면 군집존재, 0 은 빈칸
                tlst = bfs(v, si, sj)
                glst.append(tlst)
    # glst : [ [id, [r,c], [r,c], ...], [id, ...], ...]
    return glst

# 1. 입력으로 받은 직사각형 영역을 이번 실험 번호 n으로 전부 칠함
def arr_input():
    sj,si,ej,ei = map(int,input().split())
    for i in range(si,ei):  # 세로(r) 구간 [si, ei)
        for j in range(sj, ej): # 가로(c) 구간 [sj, ej)
            arr[i][j]=n # 이번 실험 번호 n으로 '덮어쓰기' -> 그 칸에 있던 예전 미생물은 사라짐

# 4. 같은 아이디가 여러 군집으로 나뉘면 그 아이디 전부 삭제
# 그 다음, 넓이 큰 순, 같으면 먼저 투입(아이디 작은) 순으로 정렬
def del_sort(glst):
    del_set = set()  # 삭제할 '군집 인덱스' 모음
    for i in range(len(glst)-1):
        for j in range(i+1, len(glst)):
            if glst[i][0]==glst[j][0]:  # 같은 아이디 군집이 2개 이상이면 '분할 발생'
                del_set.add(i) # 삭제할 군집 인덱스에 둘 다 추가
                del_set.add(j)
    # 뒤에서 앞으로 지워야 인덱스 안 꼬임
    for i in range(len(glst)-1, -1, -1):
        if i in del_set:
            glst.pop(i)
    # 배치 우선순위: (크기 큰 순, 아이디 작은 순)
    glst.sort(key=lambda x: (-len(x),x[0]))

    # 각 군집의 좌표를 '좌상단 기준(0,0)' 상대 좌표로 바꿈(모양 고정)
    for lst in glst:
        si, sj = N, N # 각 군집에서 행 최소값 = si, 열 최소값 = sj를 찾음 => 좌상단 꼭짓점
        for ci, cj in lst[1:]:  # [0]은 아이디, [1:]은 좌표들
            si = min(si, ci)
            sj = min(sj, cj)
        # 좌상단을 (0,0)에 오도록 평행이동
        for idx in range(1, len(lst)):
            lst[idx][0]-=si # 좌표에 -si, -sj를 더해서 좌상단을 (0,0)으로 이동시킴
            lst[idx][1]-=sj
    return glst

# 6. 배치 가능 여부 확인
# (si,sj) 자리를 후보에 두고, 군집 내 모든 좌표 (ci,cj)를 (si+ci, sj+cj)에 실제로 배치할 수 있는지 검사
def check(arr, lst):
    for sj in range(N): # 열을 먼저 돌고
        for si in range(N): # 행을 나중에 돎
            for ci, cj in lst:
                # 격자 범위내, 해당 칸ㅋ 빈칸
                if si+ci>=N or sj+cj>=N or arr[si+ci][sj+cj]!=0:
                    break
            else:
                return si,sj    # 가능한 자리 찾으면 (si,sj) 반환
    return -1, -1   # 못찾으면 반환

# 5. 정렬된 순서대로 한 군집씩 새통에 모양 그대로 올려둠, 못 올리면 소멸
def move(glst):
    narr = [[0]*N for _ in range(N)] # 빈 새 통 생성
    for lst in glst: # 정렬된 순서(크기 큰 것 -> 아이디 작은 것)로 한 군집씩 처리
        sn = lst[0] # 군집의 아이디
        si, sj = check(narr, lst[1:]) # 이 군집의 좌상단 기준 좌표를 새 통에서 찾음
        if (si,sj) != (-1,-1): # 이 군집의 좌상단 기준 좌표를 새통에서 찾음, (-1, -1)이면 못 놓으니까 소멸
            for ci, cj in lst[1:]: # 가능하면 군집좌표들을 (si, sj) 기준으로 평행이동시켜 실제 격자에 찍음
                narr[si+ci][sj+cj]=sn
    return narr # 새로운 통 상태 반환

# 8. (si, sj)가 속한 그 군집의 전체 크기를 셈
def bfs_adj(v, si, sj):
    # 같은 값일 때 그 개수 세고 리턴
    q = deque()
    q.append((si,sj))   # 시작 좌표 큐에 넣기
    v[si][sj] = 1   # 방문표시(이 함수 전용 방문배열 v)
    cnt = 1 # 현재까지 발견한 칸 수

    while q:
        ci, cj = q.popleft()
        # 네방향, 범위내, 미방문, 조건(같은 값)
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[si][sj]==arr[ni][nj]:
                q.append((ni,nj))   # 같은 군집이면 계속 확장
                v[ni][nj]=1 # 방문표시
                cnt+=1  # 크기 +1
    return cnt

# 7. 내 군집 크기 + 맞닿아 있는 다른 군집들의 크기 리스트를 구해 곱의 합
def bfs_score(v, si, sj):
    q = deque()
    w = [[0]*N for _ in range(N)]   # '이웃 군집' 방문 표시(중복 방지)
    cnts = []   # 이웃 군집들의 크기 목록

    q.append((si,sj))
    v[si][sj] = 1   # '내 군집' 방문 표시
    mycnt = 1   # 내 군집 크기 카운터

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                if arr[ni][nj]==arr[si][sj]:    # 같은 군집이면 내 크기 증가
                    q.append((ni,nj))
                    v[ni][nj]=1
                    mycnt+=1
                elif arr[ni][nj]>0 and w[ni][nj]==0:    # 다른 군집 처음 만나면
                    tcnt = bfs_adj(w,ni,nj) # 그 군집 크기 한 번만 세기
                    cnts.append(tcnt)
    ans = 0
    for cnt in cnts:
        ans += mycnt*cnt
    return ans

# 9. 점수 합산
def score(arr):
    v = [[0]*N for _ in range(N)]   # 내 군집 방문표시
    ans = 0
    for si in range(N):
        for sj in range(N):
            if v[si][sj]==0 and arr[si][sj]>0:  # 미방문 + 군집이 있는 칸이면
                t = bfs_score(v, si, sj)    # 그 군집 기준 점수
                ans+=t
    return ans

N, Q = map(int, input().split())
arr = [[0] * N for _ in range(N)]

for n in range(1, Q+1): # n은 실험 번호
    # [1] 이번 직사각형 ' 덮어쓰기' - 이번 실험 번호 n으로 칠함
    arr_input()

    # [2] 현재 격자에서 군집들을 전부 뽑기
    glst = group()

    # [3] 분할 소멸(같은 아이디 2개 이상 -> 전멸), 정렬(크기↓, 아이디↑), 상대좌표화
    glst = del_sort(glst)

    # [4] 큰 것/먼저 온 것부터 새 통에 모양 유지로 배치(못 놓으면 소멸)
    arr = move(glst)

    # [5] 점수 계산(인접 군집 면적 곱 합)
    ans = score(arr)

    print(ans)