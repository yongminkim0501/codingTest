n = int(input())
a = map(int, input().split(" ")) 
count = 0
for i in a:
  flag =True
  if i == 1 or (i % 2 == 0 and i != 2):
    flag = False
  for j in range(2,i):
    if i%j == 0:
      flag = False
      break
  if flag == True :
    count += 1

print(count)
     
    
     
