N = int(input())
number = map(int, input().split())
count = 0

for num in number:
  if num > 1:
    for j in range(2, num):
      if num % j == 0:
        break
    else:
      count += 1

print(count)
