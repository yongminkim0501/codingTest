first = float(input())

while True:
    temp = float(input())
    
    if temp == 999:
        break
        
    print('%.2f' % (temp - first))
    
    first = temp