# 첫째 줄에 문자열의 개수 N과 M이 주어짐
# 다음 n개의 줄에는 집합 s에 포함되어 있는 문자열들이 주어짐
# 다음 M개의 줄에는 검사해야 하는 문자열들이 주어짐
# 입력으로 주어지는 m개의 문자열 중에서 집합 s에 포함되어 있는 것이 총 몇 개인지 구하시오
import sys
n, m = map(int, input().split(" "))

text_list = []
text_set = set()
for i in range(n):
    str_input = sys.stdin.readline().strip()
    text_list.append(str_input)

text_set = set(text_list)
result_count = 0
for i in range(m):
    str_input = sys.stdin.readline().strip()
    if str_input in text_set:
        result_count += 1

if __name__ == "__main__":
    print(result_count)