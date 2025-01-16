'''
사람들이 만난 기록이 시간 순서대로 n개 주어짐

춤 추지 않고 있던 사람이 춤 추고 있는 사람을 만나게 되면, 춤을 추게 됨

기록이 시작되기 이전 춤 추고 있는 사람은 1명일 때,
마지막 기록 이후 무지개 댄스를 추는 사람이 몇명인지

예제 입력 1:
12
bnb2011 chansol
chansol chogahui05
chogahui05 @jthis
jthis <ChongChong>
@jthis @jyheo98
@jyheo98 @lms0806
@lms0806 @pichulia
@pichulia @pjshwa
@pjshwa r4pidstart
r4pidstart swoon
swoon tony9402
tony9402 bnb2011

ChongChong 이게 총총이
'''
import sys
n = int(sys.stdin.readline())
result = []
flag = False
for _ in range(n):
    a,b = sys.stdin.readline().split()
    if flag == True:
        if a not in result and b in result:
            result.append(a)
        elif b not in result and a in result:
            result.append(b)
    else:
        if a == "ChongChong" or b == "ChongChong":
            if a == "ChongChong":
                result.append(b)
            else:
                result.append(a)
            result.append("ChongChong")
            flag = True
print(len(result))