'''fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때,
 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.'''
# fib (4) -> fib(3) + fib(2)
# fib (3) -> fib(2) + fib(1)
# fib (2) -> fib(1) + fib(0)
# 이러면 1은 2번 0은 1번 출력됨.
# (a, b) : a는 fib(1) 이 나온 횟수, b는 fib(0)이 나온 횟수
# fib (0) => (0,1)
# fib (1) => (1,0)
# fib (2) => (1,1)
# fib (3) => (2,1)
# fib (4) => (3,2) : fib(3) + fib(2)
'''첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
0
1
3
'''
dp = [[0, 0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
dp[2] = [1,1]
t = int(input())
for _ in range(t):
    tmp = int(input())
    if tmp >= 3:
      for i in range(3,tmp+1):
        if dp[i] == [0,0]:
          dp[i][0] = dp[i-1][0] + dp[i-2][0]
          dp[i][1] = dp[i-1][1] + dp[i-2][1]
      print(dp[tmp][0], dp[tmp][1])
    else:
      print(dp[tmp][0], dp[tmp][1])