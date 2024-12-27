n = int(input())
count = 0
d = 665
while (count != n):
    d += 1
    tmp = str(d)
    for i in range (len(tmp)-3 + 1):
        if tmp[i:i+3] == '666':
            count += 1
            break
        
print(d)