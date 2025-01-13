n = int(input())
'''
들어올 수 있는 명령 종류
add x : s에 x를 추가, s에 x가 이미 있으면 무시
remove x : s에서 x를 제거한다, x가 없는 경우 연산을 무시한다.
check x : s에 x가 있으면 1, 없으면 0을 출력한다
toggle x : S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다
all : s를 {1, 2, ..., 20} 으로 바꾼다
empty : s를 공집합으로 바꾼다

집합의 요소 추가
s1.add(@)
s1.remove(@)
# 요소가 없으면 KeyError 발생
s1.discard(@)
# 요소가 없어도 에러 발생 x
'''
import sys
arr = set()
for _ in range(n):
    tmp = sys.stdin.readline().split()
    if len(tmp) != 1 :
        value = int(tmp[1])
        if tmp[0] == "add":
            arr.add(value)
        elif tmp[0] == "remove":
            arr.discard(value)
        elif tmp[0] == "check":
            if value in arr:
                print(1)
            else:
                print(0)
        else:
            if value in arr:
                arr.discard(value)
            else:
                arr.add(value)
    else:
        if tmp[0] == "all":
            arr = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        else:
            arr = set()
