# 풀이 1
def solution(a, b):
    A = int(str(a) + str(b))
    B = 2 * a * b
    if  A != B:
        answer = max(A, B)  
    else:
        answer = A
    return answer

# 풀이 2
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)