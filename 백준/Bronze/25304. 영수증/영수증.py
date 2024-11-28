price = int(input())

n = int(input())
sum_t = 0
for _ in range(n):
  tmp = list(map(int, input().split(" ")))
  sum_t += (tmp[0]*tmp[1])

if price == sum_t : print("Yes")
else: print("No")