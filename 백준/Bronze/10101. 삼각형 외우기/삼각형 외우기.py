e = []
flag_equil = 0
sum = 0
for i in range(3):
  k = int(input())
  e.append(k)
  sum += k

if sum != 180:
  print("Error")
else:
  if e[0] == e[1]:
    if e[1] == e[2]:
      print("Equilateral")
    else: #e[1] != e[2]
      print("Isosceles")
  elif e[0] == e[2]: #e[0] == e[2] / e0 e1 e2 가 같은 경우는 위에서 이미 분리됨
    print("Isosceles") # 그렇기 떄문에 2변이 같은 경우로 판별
  elif e[1] == e[2]:
    print("Isosceles") # e0 == e1이 아니고 e0 == e2 가 아니면, 
  else:
    print("Scalene")
