result = []
for _ in range(7):
    temp = int(input())
    if temp % 2 != 0:
        result.append(temp)
if len(result) != 0 :
    print(sum(result))
    print(min(result))
else:
    print(-1)