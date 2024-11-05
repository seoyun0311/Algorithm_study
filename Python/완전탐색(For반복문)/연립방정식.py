
A, B, C, D, E, F= map(int, input().split())

for X in range(-10000, 10000):
  for Y in range(-10000, 10000):
    if A*X + B*Y == C:
      if D*X + E*Y == F:
        print(X, Y)
        break