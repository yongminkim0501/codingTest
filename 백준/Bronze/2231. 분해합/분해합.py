n = input() # n과 각 자리 수의 합
flag = False
for i in range(int(n)):
  if int(n) == 1:
    print(0)
    flag = True
    break
  a = 0
  k = str(i)
  for j in k:
    a += int(j)
  a += i
  if a == int(n):
    print(i)
    flag = True
    break

if flag == False:
  print(0)
