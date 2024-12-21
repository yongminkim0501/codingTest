import sys
from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
    def push(self, a):
        self.q.append(a)
    def pop(self):
        if len(self.q) == 0:
            return -1
        else:
            return self.q.popleft()
    def size(self):
        return len(self.q)
    def empty(self):
        if len(self.q) == 0 : return 1
        else: return 0
    def front(self):
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]
    def back(self):
        if len(self.q) == 0:
            return -1
        else:   
            return self.q[-1]
n = int(sys.stdin.readline().rstrip())
qu = Queue()
for _ in range (n):
    tmp = sys.stdin.readline().rstrip().split()
    if len(tmp) != 1 :
        num = int(tmp[1])
        qu.push(num)
    else:
        if tmp[0] == 'pop':
            print(qu.pop())
        elif tmp[0] == 'size':
            print(qu.size())
        elif tmp[0] == 'empty':
            print(qu.empty())
        elif tmp[0] == 'front':
            print(qu.front())
        elif tmp[0] == 'back':  
            print(qu.back())


