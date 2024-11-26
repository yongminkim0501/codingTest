n = int(input())
result = 1
for i in range (1,n+1):
  result *= i

result = str(result)
count = 0
for i in range(len(result)):
  if result[i] == '0':
    count += 1
  else:
    break
i = len(result) - 1

while(True):
  if result[i] == '0':
    i -= 1
    count += 1
  else:
    break
  if i == 0:
    break

print(count)