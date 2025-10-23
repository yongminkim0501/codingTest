# 숫자 카드 N개, 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램

# 첫 줄 : 숫자 카드 개수 N
# 두번쨰 줄 : 숫자 카드에 적혀있는 정수
# 셋째 줄 : M
# 넷째 줄 : 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 m개의 정수
import sys

n = int(input())

num_list = set(map(int,sys.stdin.readline().split()))
m = int(input())
check_list = set(map(int,sys.stdin.readline().split()))
check_dict = {}

for item in check_list:
    if item in num_list: # -> 이 부분의 연산 시, set (집합) 연산을 사용하게 되면 시간 복잡도가 O(1)이 나오게 됨
        check_dict[item] = 1
    else:
        check_dict[item] = 0
if __name__ == "__main__":
    print(' '.join(map(str, check_dict.values())))