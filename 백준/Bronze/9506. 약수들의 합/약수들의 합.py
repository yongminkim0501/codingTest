while(True):
    n = int(input())
    arr = []
    brr = 0
    if n == -1 :
        exit(0)
    else:
        for i in range(1, n//2+1):
            if n % i == 0:
                brr += i
                arr.append(i)
        if brr == n :
            print(f"{n} = ", end="")
            for i in arr:
                if i == arr[-1]:
                    print(f"{i}")
                else:
                    print(f"{i}", end = "")
                    print(" + ", end ="")
                    if i == arr[-1]:
                        print(f"{i}")
        else:
            print(f"{n} is NOT perfect.")
            
