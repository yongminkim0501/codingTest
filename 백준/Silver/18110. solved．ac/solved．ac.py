import sys
def round_1 (x):
  if x - int(x) >= 0.5:
    return int(x) + 1
  else:
    return int(x)
a = int(sys.stdin.readline())
if a == 1:
 tmp = int(sys.stdin.readline())
 print(tmp)
elif a == 0:
  print(0)
else:
  b = []
  for i in range(a):
    b.append(int(sys.stdin.readline()))

  b.sort()
  c = round_1(len(b) * (15/100))
  b = b[c:len(b)-c]
  print(round_1(sum(b)/len(b)))