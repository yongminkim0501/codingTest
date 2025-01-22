while(True):
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        exit(0)
    else:
        arr = [a,b,c]
        arr.sort()
        if arr[2] >= arr[0] + arr[1]:
            print("Invalid")
        else:
            if arr[2] == arr[0] and arr[0] == arr[1] :
                print("Equilateral")
            elif (a == b and a != c) or (a == c and a != b) or (b == c and a != c) :
                print("Isosceles")
            else:
                print("Scalene")