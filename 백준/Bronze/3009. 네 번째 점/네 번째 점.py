x1, y1 = map(int, input().split(" "))
x2, y2 = map(int, input().split(" "))
x3, y3 = map(int, input().split(" "))


if x1 == x2:
  if y1 == y3:
    print(x3,y2)
  else:
    print(x3,y1)
elif x1 == x3:
  if y1 == y2:
    print(x2, y3)
  else:
    print(x2, y1)

else: # x2 == x3
  if y2 == y1 :
    print(x1, y3)
  else:
    print(x1, y2)