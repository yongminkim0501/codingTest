n = int(input())
for i in range(n):
  t, s = input().split(" ")
  t = int(t)
  for item in s:
    print(item*t, end ="")
  print()