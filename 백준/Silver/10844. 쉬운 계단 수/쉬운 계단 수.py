n = int(input())
MOD = 1000000000

if n == 1:
    print(9)
else:
    dp = [1]*10
    dp[0] = 0
    
    for i in range(1, n):
        next_dp = [0]*10
        for j in range(10):
            if j == 0:
                next_dp[j] = dp[1]
            elif j == 9:
                next_dp[j] = dp[8]
            else:
                next_dp[j] = dp[j-1] + dp[j+1]
            next_dp[j] %= MOD
        dp = next_dp
            
    print(sum(dp) % MOD)
