n = int(input())
a = list(map(int, input().split(" ")))
t, p = map(int, input().split(" "))
t_count = 0
p_count = 0
pen = 0
for item in a:
  if item % t == 0:
    t_count += item//t
  else:
    t_count += item//t + 1
  
if n % p == 0:
  p_count += n//p
  pen = 0
else :
  p_count += n//p
  pen = n%p

print(t_count)
print(p_count, pen)