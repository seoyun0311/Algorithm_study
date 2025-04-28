while True:
  try:
    n = int(input())
  except:
    break

  if n % 2 == 0 and n % 5 == 0:
    continue

  number = 1
  count = 1

  while number % n != 0:
    number = (number * 10 + 1) % n
    count += 1

  print(count)

