n = int(input())
dp = [0,1] # dp에 들어가는 값은 들어가는 숫자 개수

for i in range(2, n+1):
    min_value = 100000000
    j = 1

    while (j*j) <= i: # j가 1부터 탐색하여 j**2이 i보다 작을때까지 키워가며 찾음
        min_value = min(min_value, dp[i - (j**2)]) # min_value에 min_value와 dp[i - (j**2)] 중 작은 값을 집어 넣음
        j += 1

    dp.append(min_value + 1) # 숫자가 추가되는 개념이므로 +1

print(dp[n])