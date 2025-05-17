# 풀이 1
def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer



# 풀이 2
def solution(arr):
    stack = []
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
    return stack
