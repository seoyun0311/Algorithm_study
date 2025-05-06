import math
import sys

def sieve_of_eratosthenes(n):
  prime = [True for _ in range(n+1)]
  prime[0] = prime[1] = False
  for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i] == True:
      for j in range(i*i, n+1, i):
        prime[j] = False
  return prime

max_n = 1000000
prime_list = sieve_of_eratosthenes(max_n)

while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  for i in range(3, int(n/2)+1, 2):
    if prime_list[i] and prime_list[n-i]:
      print(f"{n} = {i} + {n-i}")
      break
  else:
    print("Goldbach's conjecture is wrong.")