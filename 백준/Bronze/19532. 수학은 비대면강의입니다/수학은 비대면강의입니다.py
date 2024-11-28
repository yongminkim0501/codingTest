import sys
A, B, C, D, E, F = map(int, sys.stdin.readline().split())
for X in range(-999, 1000):
    for Y in range(-999, 1000):
        if(A*X + B*Y == C and D*X+E*Y == F):
            print(X, Y)
            break