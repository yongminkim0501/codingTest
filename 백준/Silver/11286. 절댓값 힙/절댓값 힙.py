import sys
import heapq
'''
절댓값 힙

다음과 같은 연산을 지원하는 자료구조
1. 배열에 정수 x (x!=0)를 넣는다
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
- 절댓값이 가장 작은 값이 여러개 일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
'''
def main():
    num = int(sys.stdin.readline())
    heap = []
    for i in range(num):
        insert_num = int(sys.stdin.readline())
        if insert_num > 0 :
            sign = insert_num
            data = insert_num
        else:
            sign = abs(insert_num)
            data = insert_num

        if insert_num == 0 :
            if len(heap) == 0:
                print(f"0")
            else:
                sign, data  = heapq.heappop(heap)

                if sign >= 0:
                    print(f"{data}")
                else:
                    print(f"{data * (-1)}")
        elif insert_num != 0 :
            heapq.heappush(heap, (sign, data))

if __name__ == "__main__":
    main()