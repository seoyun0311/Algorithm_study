import itertools 

def solution(numbers):
    nums = list(numbers) 
    num = []
    for i in range(len(nums)):
        for j in itertools.permutations(nums, i+1):
            num.append(int(''.join(j)))
    num_list = list(set(num))
    
    
    answer = 0
    for i in num_list:
        if i >= 2:
            cnt = 0
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    cnt += 1
            if cnt == 0:
                answer += 1
            

        
    return answer     