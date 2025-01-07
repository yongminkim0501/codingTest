test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    
    queue = [(priority, idx) for idx, priority in enumerate(p)]
    count = 0
    
    while queue:
        current = queue[0]
        
        if any(current[0] < item[0] for item in queue[1:]): # 하나라도 true인 게 있으면, true
            queue.append(queue.pop(0))
        else:
            count += 1
            if current[1] == m:
                print(count)
                break
            queue.pop(0)
