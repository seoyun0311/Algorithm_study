from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = deque()
q.append(1)
while q:
  node = q.popleft()
  visited[node] = 1
  for nxt in graph[node]:
    if visited[nxt] == 1:
      q.append(nxt)

print(sum(visited) - 1)




