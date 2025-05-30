def solution(n, m, section):
    wall = [0] * n
    for i in section:
        wall[i-1] = 1
    paint = 0
    for i in range(1, n+1):
        if wall[i-1] == 1:
            for j in range(i-1, min(i-1+m, n)):
                wall[j] = 0
            paint += 1
    return paint
