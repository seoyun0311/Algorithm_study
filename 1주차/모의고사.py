def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5] 
    b = [2, 1, 2, 3, 2, 4, 2, 5] 
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    score_a = 0
    score_b = 0
    score_c = 0
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            score_a += 1
        if answers[i] == b[i % len(b)]:
            score_b += 1
        if answers[i] == c[i % len(c)]:
            score_c += 1
            
    max_score = max(score_a, score_b, score_c)
    answer = []

    if score_a == max_score:
        answer.append(1)
    if score_b == max_score:
        answer.append(2)
    if score_c == max_score:
        answer.append(3)
        
    return answer

