'''
최대 힙 (max heap)
최대 트리는 각 노드의 키 값이 그 자식의 키 값보다 작지 않은 트리
최대 힙은 최대 트리이면서 완전 이진 트리

최소 힙은 그에 반대

완전 이진 트리란,
노드가 삽입할 때, 왼쪽부터 차례대로 삽입하는 트리
1
2 3
45 67 이건 완전 이진 트리

1
2 3
 4 56 이건 완전 이진 트리 아님

 최대 힙에서의 삽입
 
 최대힙은 완전 이진트리를 따르기 때문에 하나의 원소를 추가시킨다면 그림 3(b) 처럼 됨
[그림 3]
      21
   15  20
 14 10 2 (30)
부모 노드보다 값이 클 경우, 서로 교환하면서 위로 올라가는 과정을 반복

최대 힙에서의 삭제
최대 힙에서 원소를 삭제할 때는 힙의 루트에서 삭제
예시로 그림 3에서 원소를 삭제한다면 루트 노드에 있는 숫자 21이 삭제

11279번 최대 힙 문제,
1. 배열에 자연수 x를 넣는다
2. 배열에서 가장 큰 값을 출력, 그 값을 배열에서 제거

만약 x가 자연수라면 배열에 x라는 값을 넣는 연산,
x가 0이라면 배열에서 가장 큰 값을 출력
그 값을 배열에서 제거

즉, 입력으로 걸러야 하는 것은 0과 나머지
0이면 Root(가장 큰 값)을 제거하고 반환

그러면 일단 root -> left, right로 연결
root가 제거되면
root의 left와 Right 중 큰 값(right)라는 가정 하에

right가 root
기존 right
  '''
import sys
from heapq import heappush, heappop
n = int(input())
arr = []
for _ in range (n):
    a = int(sys.stdin.readline())
    if a == 0 :
        if len(arr) == 0:
            print(0)
        else:
          tmp = heappop(arr)
          print(-tmp)
    else:
        heappush(arr, -a)
    


def up_heapify(index, heap):
    child_index = index
    while child_index != 0: # child Index가 0이 아니라면,
        parent_index = (child_index - 1) // 2 
        '''
        parentindex 는 child_index - 1 // 2 +> child_index가 1 or 2 이라면
        parentindex는 1-1//2 => 0, 2-1 // 2 => 0 이라서 index 0
        parentindex가 0이면 child 2가지 index는 1, 2
        parentindex가 1이면 Child_index는 3,4
        parentindex가 2이면 Child_index는 5,6
        ...

        '''
        if heap[parent_index] < heap[child_index]:
            '''
            heap의 부모 값이 자식 값보다 작다면 
            '''
            heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
            # heap의 parent와 child 위치를 바꿈
            child_index = parent_index
            # 그리고 바꿨기 때문에 index 위치도 바뀜
        else:
            return
        
        #heapq는 완전 이진 트리이지만, node등으로 구현하여 사용하는 것이 아닌 단순히 
        #배열에 값을 넣고 index로 접근함.
