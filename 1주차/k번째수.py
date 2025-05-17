# 풀이 1
array = list(map(int, input().split()))
commands = eval(input())

result = []      
for i, j, k in commands:
    arr = array[i-1:j]  
    arr2 = sorted(arr)
print(result)

# 풀이 2
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced = array[i-1:j]
        sorted_sliced = sorted(sliced)
        answer.append(sorted_sliced[k-1])
    return answer

