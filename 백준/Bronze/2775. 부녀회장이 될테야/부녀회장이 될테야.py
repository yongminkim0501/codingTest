def compare(x):
    s = 0
    d = []
    for i in x:
        s += i
        d.append(s)
    return d

t=int(input())
for _ in range(t):
    k=int(input())
    n=int(input())
    
    d=[]
    for i in range(1,n+1):
         d.append(i)

    if k>1:
        for _ in range(k-1):
            d=compare(d)
    print(sum(d))
