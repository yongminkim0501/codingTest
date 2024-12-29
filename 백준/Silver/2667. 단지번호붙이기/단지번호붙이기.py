import sys

n = int(input())

arr = []
for _ in range(n):
    tmp1 = sys.stdin.readline()
    tmp = list(tmp1)
    tmp.pop()                                       # 마지막 부분은 \n 이기 때문에 삭제
    arr.append(tmp)                                 # arr 배열에 전부 저장

for i in range(n):
    for j in range(n):
        arr[i][j] = int(arr[i][j])
       
# j가 이동할 수 있는 것 1, -1
# i가 이동할 수 있는 것 1, -1
# 동시에 이동할 수 없음, 하나만 이동해야함.
move_i = [0,0,1,-1]
move_j = [1,-1,0,0]
count = 0
result = []
def dfs(i,j):
    global count
    if i < 0 or i > n-1 or j < 0 or j > n-1:        # i, j가 범위를 벗어나면 False 반환
        return False
    else:
        if arr[i][j] == 1:
            count += 1
            arr[i][j] = 0
            for k in range(4):
                #i만 이동하거나
                #j만 이동하거나
                tmp_i = i + move_i[k]
                tmp_j = j + move_j[k]
                dfs(tmp_i, tmp_j)
            return True
        return True
    
for i in range (n):
    for j in range(n):
        if arr[i][j] == 1:
            dfs(i,j)
        result.append(count)
        count = 0

while 0 in result:
    result.remove(0)

result.sort()
print(len(result))
for i in result:
    print(i)