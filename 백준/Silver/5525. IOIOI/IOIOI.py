n = int(input()) # n+1개의 I와 n개의 O로 이루어져 있음
m = int(input()) # s의 길이 m / 마지막 3번째 줄이 s
s = input()
'''
P1 = IOI
p2 = IOIOI

S안에 Pn이 몇 군데 포함되어 있는지 구하는 프로그램 작성
만약 n이 1이라면,
P1이 몇 개 들어 있는지

n이 2라면,
P2가 몇 개 들어 있는지 ...
'''
n_text = "IO"*n+"I"
count = 0
compare_text = ""
for i in range(m-(2*n+1)+1):
    if s[i] == 'I':
        for j in range(len(n_text)):
            compare_text += s[i+j]
        if compare_text == n_text:
            count += 1

        compare_text = ""

if __name__ == "__main__":
    print(count)