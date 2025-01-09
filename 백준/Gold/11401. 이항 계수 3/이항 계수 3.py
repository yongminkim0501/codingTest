'''
페르마 소정리
a^(p-1) = 1 (mod p)
nCr = n! / ((n-r)! * r!) -> @

페르마 소정리를 사용하면
a^(p-1) = 1 mod p

((n-r)!r!)((n-r)!r!)^(p-2) = 1 mod p

모듈러 곱셈 역원
a의 곱셈의 역원이란, a와 곱해서 1이 되는 수
mod p에 대해서 곱셈의 역원은 어떻게 정의?
a * x = 1 (mod p) 을 만족하는 x이다.

((n-r)!r!)((n-r)!r!)^(p-2) = 1 mod p
((n-r)!r!)^(p-2) = ((n-r)!r!)^-1 mod p
n!((n-r)!r!)^(p-2) = n!((n-r)!r!)^-1 mod p
우변이 nCr과 같으므로
n!((n-r)!r!)^(p-2) = nCr (mod p)
nCr 을 p로 나눈 나머지는 n!((n-r)!r!)^(p-2)와 같음

p가 매우 큰 소수라면, ((n-r)!r!)^(p-2)을 구하는데도 시간이 너무 오래 걸림
-> 분할 정복을 이용한 거듭제곱 알고리즘 사용

5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
'''
import sys
sys.setrecursionlimit(10**5)
# 10 ** 5 : recursionError
# 10 ** 6 : 메모리 초과
n, k = map(int, sys.stdin.readline().split())

prime_number = 1000000007
dp = [0] * (n+1)
dp[1] = 1

def divide_fac(n,m):
    if n == m:
        return n
    if m < n:
        return 1
    else:
        return divide_fac(n , (n+m)//2) * divide_fac((n+m)//2+1,m) % prime_number

tmp = divide_fac(1,n) # 5, n은 5이고 k는 2
tmp1 = divide_fac(1,n-k) # 3
tmp2 = divide_fac(1,k) # 2

def divide_pow(a, x):
    if x == 0:
        return 1
    if x == 1:
        return a % prime_number
    
    half = divide_pow(a, x//2) % prime_number
    
    if x % 2 == 0:
        return (half * half) % prime_number
    else:
        return (half * half * a) % prime_number

print((tmp*divide_pow(tmp1 * tmp2, prime_number-2))%prime_number)

        

