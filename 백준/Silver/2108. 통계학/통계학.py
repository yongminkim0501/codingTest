import sys
n = int(input())
arr = []
count = 0
temp = {}
for _ in range (n):
    tmp = int(sys.stdin.readline())
    arr.append(tmp)
    count += tmp
    if tmp not in temp:
        temp[tmp] = 1
    else:
        temp[tmp] += 1

arr.sort()
sorted_temp = sorted(temp.items(), key=lambda x: (-x[1], x[0]))

print(round(count / n)) # 산술 평균
print(int(arr[n//2]))  # 중앙 값
if len(sorted_temp) > 1 and sorted_temp[0][1] == sorted_temp[1][1]:
    print(sorted_temp[1][0])  # 두 번째로 작은 값 출력
else:
    print(sorted_temp[0][0])
print(arr[-1]-arr[0])  # 범위
