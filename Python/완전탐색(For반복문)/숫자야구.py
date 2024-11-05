n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for a in range(1, 10):
  for b in range(10):
    for c in range(10):
      if (a == b or b == c or c == a):
        continue

      cnt = 0
# [number ball strike]
      for arr in hint:
        number = str(arr[0])
        ball = arr[1]
        strike = arr[2]

        ans = [str(a), str(b), str(c)]
        ball_count = 0
        strike_count = 0

        for i in range(3):
          if ans[i] == number[i]:
            strike_count += 1
          elif ans[i] in number:
            ball_count += 1

        if ball == ball_count and strike == strike_count:
          cnt += 1

    if cnt == n:
      answer += 1

print(answer)