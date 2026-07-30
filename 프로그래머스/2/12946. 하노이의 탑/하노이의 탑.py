answer = []

def hanoi(n, start, move, end):
    if n == 1 : 
      answer.append([start, end])
      return answer
    hanoi(n-1, start, end, move)
    hanoi(1, start, move, end)
    hanoi(n-1, move, start, end)

def solution(n):
    hanoi(n, 1, 2, 3)
    
    return answer