# 풀이 1
def solution(s):
    answer = True
    j = 0  # 루프 밖에서 초기화해야 누적 가능
    for i in s:
        if i == 'p' or i == 'P':
            j += 1
        elif i == 'y' or i == 'Y':
            j -= 1
    if j == 0:
        return answer
    else:
        return False

# 풀이 2
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
