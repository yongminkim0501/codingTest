def solution(n):
    answer = 0
    
    if n % 2 == 0:
        for idx in range(1, n+1):
            if idx % 2 == 0:
                answer += idx ** 2
    else:
        for idx in range(1, n+1):
            if idx % 2 != 0 :
                answer +=idx
    
    
    return answer