'''
지민이는 자신의 저택에서 mn개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다.
어떤 정사각형은 검은색, 나머지는 흰색
지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 함

체스판은 검 흰 번갈아 칠해져 있어야 함.
8*8 크기의 체스판으로 잘라낸 후, 몇 개의 정사각형을 다시 칠해야겠다 생각함.
최소개수를 골라라
'''
import sys
n,m = map(int,input().split())
arr = []

correct_w = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
correct_b = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B','W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W','B']]

for i in range (n):
    tmp = list(sys.stdin.readline().strip())
    arr.append(tmp)

def compare(a,b):
    global correct_b, correct_w
    count_w = 0
    count_b = 0
    
    for i in range(8):
        for j in range(8):
            if arr[a+i][b+j] != correct_w[i][j]:
                count_w += 1
            if arr[a+i][b+j] != correct_b[i][j]:
                count_b += 1
    
    return min(count_w, count_b)
    
result_temp = []
count_temp = 0

for i in range(n-7):
    for j in range(m-7):
        count_temp = compare(i, j)
        result_temp.append(count_temp)

print(min(result_temp))


