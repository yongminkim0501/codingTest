n = int(input())

a = []
for i in range (n):
  tmp = input().split(" ")
  tmp[0] = int(tmp[0])
  a.append([tmp[0], tmp[1]])

a.sort(key=lambda x:x[0])

for i in range (len(a)):
  print(f"{a[i][0]} {a[i][1]}")