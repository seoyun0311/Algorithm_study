# 몸무게 x, 키 y
N = int(input()) # 전체 사람 수
people = []

for _ in range(N):
  x, y = map(int, input().split())
  people.append((x,y))  # 리스트에 (몸무게, 키) 튜플로 저장

# people = [tuple(map(int, input().split())) for _ in range(N)] # 튜플
# people = [list(map(int, input().split())) for _ in range(N)] # 리스트

for i in people:
  rank = 1
  for j in people:
    if i[0] < j[0] and i[1] < j[1]: # 조건
      rank +=1
  print(rank, end = " ")