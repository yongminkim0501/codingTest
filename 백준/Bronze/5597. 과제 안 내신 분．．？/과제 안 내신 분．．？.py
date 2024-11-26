total = []
for i in range(1, 31):
  total.append(i)

for i in range(28):
  tmp = int(input())
  total[tmp-1] = 0

for i in range(30):
  if total[i] != 0:
    print(i+1)

