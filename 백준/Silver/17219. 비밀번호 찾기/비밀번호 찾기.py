'''
첫째 줄에 저장된 사이트 주소의 수 N, 비밀번호를 찾으려는 사이트 주소의 수 M
두번째 줄부터 N개의 줄에 걸쳐 각 줄에 사이트 주소와 비밀번호가 공백으로 구분되어 주어짐

사이트 주소는 알파벳 소문자, 알파벳 대문자, 대시('-'), 마침표('.')로 이루어져 있음.

n+2번째 줄부터 m개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한줄에 하나씩 입력
16 4
noj.am IU
acmicpc.net UAENA
startlink.io THEKINGOD
google.com ZEZE
nate.com VOICEMAIL
naver.com REDQUEEN
daum.net MODERNTIMES
utube.com BLACKOUT
zum.com LASTFANTASY
dreamwiz.com RAINDROP
hanyang.ac.kr SOMEDAY
dhlottery.co.kr BOO
duksoo.hs.kr HAVANA
hanyang-u.ms.kr OBLIVIATE
yd.es.kr LOVEATTACK
mcc.hanyang.ac.kr ADREAMER
startlink.io
acmicpc.net
noj.am
mcc.hanyang.ac.kr
'''
import sys
n, m = map(int, input().split())
arr = {}
for _ in range (n):
    address, pw = sys.stdin.readline().split()
    arr[address] = pw

for _ in range (m):
    choose_add = sys.stdin.readline().rstrip()
    print(arr[choose_add])