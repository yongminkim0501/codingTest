import sys
n = int(input())
'''
xkg ycm 이면 (x,y)로 표현
A,B의 덩치가 각각 (x,y),(p,q)라 할 때
x>p 그리고 y>q 이면 우리는 a의 덩치가 b의 덩치보다 더 크다라고 말함
어떤 a,b 두 사람의 덩치가 각각 56 177, 45 165라 하면 a의 덩치가 b보다 큼
만약 키는 한쪽이 크고 한쪽이 무게가 많이 나간다면 덩치로만 볼 때 c와 d는 누구도
상대방보다 더 크다고 말할 수 없다.

n명의 집단에서 각 사람의 덩치 등수는 자신보다 더 큰 덩치의 사람의 수로 정해짐,
만일 자신보다 더 큰 덩치의 사람이 K명 이라면, 그 사람의 덩치 등수는 K+1이 됨.
이렇게 등수를 결정하면 같은 등수를 가진 사람은 여러 명도 가능

흠... 덩치 등수를 어떻게 해야하지
'''
arr = []
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    arr.append(tmp)
# 하나를 꺼내서 이거를 나머지 경우와 비교
brr = []
for i in range (n):
    count = 1
    for j in range (n):
        if i == j:
            pass
        else:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                count += 1
            else:
                pass
    brr.append(count)

print(*brr)