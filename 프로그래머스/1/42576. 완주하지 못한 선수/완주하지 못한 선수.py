from collections import Counter
def solution(participant, completion):
    '''
    participant : 마라톤에 참여한 선수들의 이름이 담긴 배열
    completion : 완주한 선수들의 이름이 담긴 배열
    return -> 완주하지 못한 선수의 이름
    '''
    left = Counter(participant)
    right = Counter(completion)
    result = left - right
    
    answer = list(result)[0]
    
    return answer