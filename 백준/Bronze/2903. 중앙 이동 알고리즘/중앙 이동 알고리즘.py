n = int(input())


a = [2]
for i in range(1,n+1):
    a.append(2*a[i-1]-1)

print(a[n]**2)