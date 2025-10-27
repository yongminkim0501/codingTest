
def main():
    n = int(input())

    dp = [0 for _ in range(n+1)]
    # 2*n 크기의 직사각형을 1*2, 2*1 타일로 채우는 방법의 수
    '''
     2*(n)
     -> 
    만약 n을 완성한다.
    
    dp[i]인데 i = n, i가 1이라면 
    dp[1] = 1
    dp[2] = 2
    dp[3] = 
    '''

    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[-1] % 10007)

if __name__ == "__main__":
    main()