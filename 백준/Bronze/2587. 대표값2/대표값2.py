a = []
for _ in range(5):
  tmp = int(input())
  a.append(tmp)

a.sort()
mean = sum(a)/5
mid = a[2]
print(int(mean))
print(mid)
