'''
새로운 언어 AC
AC는 정수 배열에 연산을 하기 위해 만든 언어
이 언어에는 두 가지 함수 R(뒤집기), D(버리기)

함수는 조합해서 한 번에 사용할 수 있음. 예를 들어 "AB"는 A를 수행한 다음
바로 이어서 B를 수행하는 함수
"RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수

첫째 줄에 테스트 케이스의 개수 T
각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어짐, p는 1보다 크거나 같고, 100,000보다 작거나 같다
다음 줄에는 배열에 들어있는 수의 개수 n이 주어짐
다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어짐

전체 테스트 케이스에 주어지는 P의 길이의 합과 n의 합은 70만을 넘지 않음.

만약 그냥 d인 경우 첫 번째 수인데,
뒤집고 d이면 가장 마지막 수를 버리는 것

두 가지 배열을 만들어서 first_delete, final_delete를 만들어서 저장함

'''
import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    try:
        do = list(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline())
        arr = input()
        if arr == "[]":
            arr = deque()
        else:
            arr = deque(map(int, arr[1:len(arr)-1].split(",")))
        flag = True
        first_delete = 0
        final_delete= 0
        for i in do:
            if flag == True and i == "R":
                flag = False
            elif flag == False and i == "R":
                flag = True

            if i == "D" and flag == True :
                first_delete += 1 # flag == False이면 한 번 뒤집은 상태
            elif i == "D" and flag == False:
                final_delete += 1 # flag == True이면 원래 상태
        if first_delete + final_delete > len(arr):
            raise ValueError
        arr = list(arr)
        # R이 짝수번 나오면 원래 모양대로 출력 - Flag가 True임
        # R이 홀수번 나오면 뒤집어서 출력 - Flag가 False임
        # error가 발생한 경우 error 출력
        result = arr[first_delete:len(arr)-final_delete]
        if not flag:
            result.reverse()
        print("[" + ",".join(map(str, result)) + "]")
    except:
        print("error")