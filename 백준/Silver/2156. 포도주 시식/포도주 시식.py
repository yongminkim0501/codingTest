import sys
sysInput = sys.stdin.readline
N = int(sysInput())
wine = [0 for i in range(10001)]
for i in range(N):
    wine[i] = int(sysInput())
dp = [0 for i in range(10001)]
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0]+wine[2], wine[1]+wine[2], dp[1])
for i in range(3, N):
    dp[i] = max(wine[i]+wine[i-1]+dp[i-3], wine[i]+dp[i-2], dp[i-1])
print(max(dp))