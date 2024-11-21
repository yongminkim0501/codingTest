n = int(input())
a = input().split(" ")
for i in range(n): a[i] = int(a[i])
result = 0
dp= [a[0]]

for i in range(1,n):
  if dp[i-1] > 0:
    if a[i] >= 0:
      dp.append(dp[i-1] + a[i])
    else:
      if dp[i-1] + a[i] >= 0:
        dp.append(dp[i-1]+ a[i])
      else:
        dp.append(a[i])
  else:
    if a[i] > dp[i-1]:
      dp.append(a[i])
    else:
      dp.append(dp[i-1])
print(max(dp))