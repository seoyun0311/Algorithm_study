def solution(dots):
  cases = [
    (0, 1, 2, 3),
    (0, 2, 1, 3),
    (0, 3, 1, 2)
  ]
  for i1, i2, i3, i4 in cases:
    dx1 = dots[i2][0] - dots[i1][0]
    dy1 = dots[i2][1] - dots[i1][1]
    dx2 = dots[i4][0] - dots[i3][0]
    dy2 = dots[i4][1] - dots[i3][1]
        
    if dy1 * dx2 == dy2 * dx1:
      return 1
  return 0