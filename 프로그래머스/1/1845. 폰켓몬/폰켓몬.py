def solution(nums):
    '''
    nums = [3,1,2,3], [3,3,3,2,2,4],[3,3,3,2,2,2]
    '''
    dic = {}
    names = []
    for item in nums:
        if item not in names :
            names.append(item)
            dic[item] = 1
        else:
            dic[item] += 1
    
    if len(nums) // 2 > len(names):
        answer = len(names)
    else:
        answer = len(nums)//2
    return answer