from itertools import combinations
  
heights = [int(input()) for _ in range(9)]

for comb in combinations(heights, 7):
  if sum(comb) == 100:
    for h in sorted(comb):
      print(h)
    break