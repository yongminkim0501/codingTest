n = int(input())# n+1개의 I와 n개의 O로 이루어져 있음
m = int(input())# s의 길이 m / 마지막 3번째 줄이 s
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
def create_pi(pattern):
    pattern_length = len(pattern)
    pi = [0 for _ in range(pattern_length)]
    j = 0
    for i in range(1, pattern_length): #pi[0] = 0
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j+=1
            pi[i] = j
    return pi

def kmp(word, pattern):
    pi = create_pi(pattern)
    word_length = len(word)
    pattern_length = len(pattern)
    count = 0
    matched_cnt = 0
    matched_point = []

    p_idx = 0
    for w_idx in range(word_length):
        while p_idx > 0 and word[w_idx] != pattern[p_idx]:
            p_idx = pi[p_idx-1]

        if word[w_idx] == pattern[p_idx]:
            if p_idx == pattern_length-1:
                matched_cnt += 1
                matched_point.append(w_idx-pattern_length+1)
                p_idx = pi[p_idx]
            else:
                p_idx += 1

    print(matched_cnt)


if __name__ == "__main__":
    kmp(s, n_text)


'''
제약 조건 있는 것은 통과
제약 조건 없는 것은 통과 X

kmp 알고리즘을 써야 한다고 한다.
KMP는 브루트 포스와 다르게 O(N+M) 알고리즘임.

2가지 개념을 먼저 알아야 한다고 함.
단어 : korea
1. 접두사 (prefix), 접미사 (suffix)
길이 1: k | a
길이 2: ko | ea
길이 3: kor | rea ... 이런 식,

2. LPS 알고리즘
주어진 문자열의 부분 문자열들 중 가장 긴 접두사이자 접미사
KMP 알고리즘에서는 패턴의 0번쨰 인덱스가 무조건 포함되는 문자열들이 LPS길이가 활용
LPS를 구하는 과정에서 overlapping 규칙을 적용함을 전제로함
ababcaba를 예로 들면
index 0 : a / lps : 0
index 1 : ab / lps : 0
index 2 : aba / lps : 1
index 3 : abab / lps : 2
index 4 : ababc / lps : 0
index 5 : ababca / lps : 1
index 6 : ababcab / lps : 2
index 7 : abcbcaba / lps : 3

kmp는 이 두가지 전부 사용 

lps 알고리즘으로 pi 배열을 만들어주고 pi 배열을 활용해 
시간복잡도 O(n)으로 매칭되는 패턴이 어디에, 몇 개 존재하는지 알아내는 로직이다.

word : ababdababcabbababcababcababa
패턴 : ababcaba


'''