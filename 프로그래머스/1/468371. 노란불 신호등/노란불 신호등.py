import sys
from math import gcd
# 제출 확인용 깃헙 연동
input = sys.stdin.readline

def lcm(a,b):
    return a*b // gcd(a,b)

def solution(signals):

    periods = [sum(s) for s in signals]
    
    total_lcm = 1
    for p in periods:
        total_lcm = lcm(total_lcm, p)
        
    for t in range (1, total_lcm+1):
        flag = True
        for i in range(len(signals)):
            if signals[i][0] <= (t - 1) % periods[i] < signals[i][0] + signals[i][1]:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            return t
    return -1