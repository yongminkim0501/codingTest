while(True):
  a,b,c = input().split(" ")
  a = int(a)
  b = int(b)
  c = int(c)
  a *= a
  b *= b
  c *= c
  if a == 0 and b == 0 and c == 0:
    break

  if a == b+c or c == b+a or b == a+c:
    print("right")
  else:
    print("wrong")