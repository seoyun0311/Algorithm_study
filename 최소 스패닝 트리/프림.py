import heapq

# 프림
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(N):
  A, B, C = map(int, input().split())

  graph[A].append([C,B])
  graph[B].append([C,A])

# 다익스트라
answer = 0
cnt = 0

q = [[0,1]] # 가중치 없이 1에서 출발

while q: # q가 아무것도 없어질 때까지
  if cnt == N:
    break

  weight, node = heapq.heappop(q) # 최소비용을 꺼내줌

  if visited[node] == 0:
    visited[node] = 1
    answer += weight
    cnt += 1
    for nxt in graph[node]:
      heapq.heappush(q, nxt)

print(answer)