A, B = map(int, input().split())
A -= 1

tmp_A = A
for i in range(1, 99):
  tmp_A += (A//(2**i)) * ((2**i)-(2**(i-1)))

tmp_B = B
for i in range(1, 99):
  tmp_B += (B//(2**i)) * ((2**i)-(2**(i-1)))

print(tmp_B - tmp_A)