import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    answer = []
    check = days[0]
    count = 1           
    
    for d in days[1:]:
        if d <= check:
            count += 1
        else:
            answer.append(count)
            check = d    
            count = 1    
    answer.append(count)
    
    return answer