def solution(clothes):
    answer = 0
    dic = {}
    for item in clothes:
        key = item[1]
        if key in dic :
            dic[key] += 1
        else:
            dic[key] = 1
            
    dot_answer = 1
    for count in dic.values():
        dot_answer *= (count+1)

    answer += (dot_answer-1)

    return answer