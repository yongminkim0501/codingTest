'''
둘째 줄부터 n개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 n번에 해당하는 포켓몬까지 한 줄에
하나 씩 입력으로 들어옴

포켓몬 이름은 모두 영어로만 이루어져 있고,
첫 글자 대문자, 나머지 문자는 소문자

일부 포켓몬은 마지막 문자만 대문자 일 수도 있음.

그 다음 줄 부터 총 m개의 줄에 맞춰야 하는 문제가 입력으로 들어옴,
문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야하고,
숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야함
'''
n, m = map(int, input().split())
import sys
num_dic = {}
name_dic = {}
for i in range (n):
    tmp = sys.stdin.readline().rstrip()
    num_dic[i+1] = tmp
    name_dic[tmp] = i+1
for i in range (m):
    tmp = sys.stdin.readline().rstrip()
    if tmp.isdigit() == True: # 만약 입력이 숫자라면
        print(num_dic[int(tmp)])
    else: # 만약 입력이 문자열이라면
        print(name_dic[tmp])