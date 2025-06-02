# 백준 2816 "디지털 티비"
# 1번 : 화살표를 한 칸 아래로 내린다 채널 i에서 i+1로
# 2번 : 화살표를 위로 한칸 올린다 채널i에서 i-1로
# 3번 : 현재 선택한 채널을 한 칸 아래로 내린다(채널 i와 i+1의 위치를 바꾼다 화살표는 i+1을 가리키고 있음)
# 4번 : 현재 선택한 채널을 위로 한 칸 올린다(채널 i와 i-1의 위치를 바꾼다 화살표는 i-1을 가리키고 있음)
# 화살표가 채널 리스트의 범위를 넘어간다면 그 명령은 무시

N = int(input())
chn = list(input() for _ in range(N))
ans = []
cur = 0
while chn[cur] != 'KBS1': # KBS1을 발견할 때까지 1로 내려가기
  cur += 1
  ans.append(1)
for _ in range(cur): # 내려온 만큼 (=다시 맨 위로) KBS1을 올리기
  ans.append(4)
cur = 0
chn.remove('KBS1') # 원 채널 리스트에서 KBS1을 지우고 맨 앞으로 옮겨 새로운 배열 생성
chn = ['KBS1'] + chn
while chn[cur] != 'KBS2': # 마찬가지로 KBS2를 발견할 때까지 1로 내려가기
  cur += 1
  ans.append(1)
for _ in range(cur-1): # 맨 위가 아닌 두 번째 위치로 KBS2를 올리기
  ans.append(4)
print(''.join(map(str,ans)))