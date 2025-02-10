import sys

class seg_tree:
    def __init__(self, temp_arr):
        self.temp_arr = temp_arr
        self.tree = [0] * (4*len(temp_arr))
        self.build(1,0,len(temp_arr)-1)

    def build(self, node, start, end):
        if start == end :
            self.tree[node] = self.temp_arr[start]
        else:
            mid = (start + end) // 2
            self.build(2*node, start, mid)
            self.build(2*node + 1, mid+1, end)
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def update(self, index, value):
        diff = value - self.temp_arr[index]
        self.temp_arr[index] = value
        self._update(1,0,len(self.temp_arr)-1, index, diff)
    def _update(self, node, start, end, index, diff):
        if index < start or index > end:
            return # 범위 내에 없다면 제외
        self.tree[node] += diff # 차이만큼 +
        if start != end :
            mid = (start + end) // 2
            self._update(2*node,start,mid,index,diff)
            self._update(2*node+1, mid+1, end, index, diff)

    def query(self, left, right):
        # 세그먼트 트리에서 특정 구간의 값을 찾아내는 데 사용
        # 분할 정복 알고리즘을 사용
        # 먼저 찾고자 하는 구간이 트리의 현재 노드가 표현하는 구간과 완전히
        # 일치하면, 그 노드의 값을 반환
            # _query메서드를 호출하여 이를 구현하는데, 현재 노드가 나타내는 구간과
            # 특정 구간 (left~right)에 완전히 포함되는 경우는 현재 노드의 값을 반환
        # 그렇지 않다면, 노드의 두 자식 노드에 대한 정보를 이용하여, 찾고자 하는 구간을 더 작은 구간으로 분할한 다음
        # 각각 자식 노드에 대해 query메서드를 호출
        return self._query(1,0,len(self.temp_arr)-1, left, right)
    
    def _query(self, node, start, end, left, right):
        if left>end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self._query(2*node, start, mid, left, right) + self._query(2*node+1, mid + 1, end, left, right)
    
input = sys.stdin.readline
n,m,k = map(int, input().split())
# n은 숫자의 개수
# m은 수의 변경이 일어나는 횟수
# k는 구간의 합을 구하는 횟수
# 둘째 줄부터 n+1번째 줄까지 N개의 수가 주어짐
# n+2번째 줄부터 n+m+k+1 번째 줄까지 세 개의 정수 a,b,c가 주어짐
# a가 1이라면, b번째 수를 c로 바꾸고
# a가 2라면, b번째 수부터 c번째 수까지의 합을 구하여 출력
arr = []
for _ in range(n):
    temp = int(input())
    arr.append(temp)

segtree = seg_tree(arr)

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1: # a가 1이라면 b번째 수를 c로 바꿈
        segtree.update(b-1, c)
    else:
        print(segtree.query(b-1,c-1))
    