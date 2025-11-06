import sys
from collections import defaultdict
'''
과일 탕후루 -> 1~9번 번호 (각기 다른 과일)
주문을 확인해보니 과일을 두 종류 이하로 사용해달라는 요청
막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했음
앞에서 a개, 뒤에서 b개 과일을 빼면 s_a+1, s_a+2, ... , 총 N-(a+b)개가 꽂혀있는 탕후루가 됨.
이렇게 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하세요
'''
def main():
    n = int(sys.stdin.readline())
    fruits = list(map(int, sys.stdin.readline().split(" ")))
    result = 0
    fruit_count = defaultdict(int)
    a_result = 0
    for idx in range(n):
        cur_fruit = fruits[idx]
        fruit_count[cur_fruit] += 1
        while len(fruit_count) > 2:
            l_fruit = fruits[a_result]
            fruit_count[l_fruit] -= 1
            if fruit_count[l_fruit] == 0:
                del fruit_count[l_fruit]
            a_result += 1
        length = idx - a_result + 1
        result = max(length, result)
    print(result)
    '''for a in range(n):
        for b in range(n):
            len_set_fruit = len(set(fruits[a:n-b]))
            if len_set_fruit <= 2 and max_count < len(fruits[a:n-b]) :
                max_count = len(fruits[a:n-b])
                a_result, b_result = a, b'''


if __name__ == "__main__":
    main()