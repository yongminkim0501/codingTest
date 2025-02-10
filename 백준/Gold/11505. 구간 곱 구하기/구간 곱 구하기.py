import sys

class seg_tree:
    def __init__(self, temp_arr):
        self.temp_arr = temp_arr
        self.tree = [1] * (4*len(temp_arr))
        self.build(1,0,len(temp_arr)-1)

    def build(self, node, start, end):
        if start == end :
            self.tree[node] = self.temp_arr[start]
        else:
            mid = (start + end) // 2
            self.build(2*node, start, mid)
            self.build(2*node + 1, mid+1, end)
            self.tree[node] = self.tree[2*node] * self.tree[2*node+1] % 1000000007

    def update(self, index, value):
        self.temp_arr[index] = value
        self._update(1,0,len(self.temp_arr)-1, index, value)

    def _update(self, node, start, end, index, value):
        if index < start or index > end:
            return
        
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            self._update(2*node, start, mid, index, value)
            self._update(2*node+1, mid+1, end, index, value)
            self.tree[node] = (self.tree[2*node] * self.tree[2*node+1]) % 1000000007
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
            return 1
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_result = self._query(2*node, start, mid, left, right) % 1000000007
        right_result = self._query(2*node+1, mid + 1, end, left, right) % 1000000007
        return (left_result * right_result) % 1000000007
    
    def check_debug(self):
        return self.temp_arr, self.tree

input = sys.stdin.readline
'''
어떤 n개의 수가 주어져 있음. 근데 중간에 수의 변경이 빈번히 일어나고, 중간에 어떤 부분의 곱을 구하려 함
1,2,3,4,5라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번쨰까지 곱을 구하라하면
240출력

다섯번째 수를 2로 바꾸고 3번쨰부터 5번째까지 곱을 구하라고 한다면 48
'''
n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    temp = int(input())
    arr.append(temp)
segtree = seg_tree(arr)
# a가 1이면 b번째 수를 c로 바꾸고
# a가 2인 경우 b부터 c까지의 곱을 구하여 출력하면 됨
for i in range (m+k):
    a,b,c = map(int, input().split())
    if a == 1:
        segtree.update(b-1, c)
    else:
        print(segtree.query(b-1,c-1))