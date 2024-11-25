a = map(int, input().split(" "))
valid_num = 0
for i in a:
  valid_num += i*i

print(valid_num%10) 