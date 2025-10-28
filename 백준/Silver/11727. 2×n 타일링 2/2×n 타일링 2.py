def main():
    n = int(input())
    dp = [0 for _ in range(n+1)]
    if n <= 2:
        if n == 2 : print(3)
        elif n == 1 : print(1)
        else: print(1)
    else:
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
        for i in range(2, n+1):
            dp[i] = dp[i-1] + 2*dp[i-2]
            dp[i] %= 10007
        print(dp[-1])

if __name__ == "__main__":
    main()