def solution(n, w, num):
    if num % w == 0:
        temp = num // w
    else:
        temp = num // w + 1
    
    if n % w == 0:
        temp1 = n // w
    else:
        temp1 = n // w + 1
    
    if temp1 == temp:
        return 1
    
    if temp % 2 == 0: 
        if num % w == 0:
            cur = 1
        else:
            cur = w - (num % w) + 1  
    else:  
        if num % w == 0:
            cur = w
        else:
            cur = num % w
    
    if temp1 % 2 == 0:  
        if n % w == 0:
            cur1 = 1
        else:
            cur1 = w - (n % w) + 1  
    else: 
        if n % w == 0:
            cur1 = w
        else:
            cur1 = n % w
    
    result = temp1 - temp
    
    if temp1 % 2 == 0:  
        if cur1 <= cur:
            result += 1
    else:  
        if cur1 >= cur:
            result += 1
    
    return result
