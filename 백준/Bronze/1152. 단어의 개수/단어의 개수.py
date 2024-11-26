s = input().split(" ")
count = 0
for i in s:
  if i == "":
    continue
  else:
    count += 1

print(count)