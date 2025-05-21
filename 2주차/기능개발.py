def solution(progresses, speeds):
    answer = []
    days = []

    for p, s in zip(progresses, speeds):
        remain = 100 - p
        need_day = (remain + s - 1) // s 
        days.append(need_day)

    current = days[0]
    count = 1

    for d in days[1:]:
        if d <= current:
            count += 1
        else:
            answer.append(count)
            current = d
            count = 1

    answer.append(count)
    return answer
