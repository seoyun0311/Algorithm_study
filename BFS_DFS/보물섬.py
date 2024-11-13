from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

maxi = 0
for y in range(n):
  for x in range(m):
    if graph[y][x] == 'L':
      visited = [[0 for _ in range(m)] for _ in range(n)]
      dist = [[0 for _ in range(m)] for _ in range(n)]

      q = deque()
      q.append((y,x))
      visited[y][x] = 1
      
      while q:
        ey, ex = q.popleft()
        for dy, dx in [[0,1], [0,-1], [1,0], [-1,0]]:
          ny, nx = ey + dy, ex + dx
          if 0 <= ny < n and 0<= nx < m:
            if graph[ny][nx] == 'L':
              if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                dist[ny][nx] = max(dist[ey][ex] + 1, dist[ny][nx])
                if maxi < dist[ny][nx]:
                  maxi = dist[ny][nx]
                q.append((ny, nx))

print(maxi)