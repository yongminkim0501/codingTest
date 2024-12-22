class Node:
    def __init__(self, data, prev = None, next =None):
        self.data = data
        self.next = next
        self.prev = prev


class Customlinkedlist:
    def __init__(self,n):
        self.head = Node(1)
        self.tail = Node(n)
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head
        self.size = 2
        self.result = []
        
    def append(self, data):
        new_node = Node(data)
        if self.size == 2:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.next = self.tail
            new_node.prev = self.head
        else:
            tmp = self.tail.prev
            new_node = Node(data, next = self.tail, prev = tmp)
            tmp.next = new_node
            self.tail.prev = new_node
        self.size += 1


    def search(self,n, k):
        cur = self.head.prev
        result = []
        while(len(result) != n):
            for i in range(k):
                cur = cur.next
            result.append(cur.data)
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        return result

n, k = map(int, input().split())

data = Customlinkedlist(n)
for i in range(2,n):
    data.append(i)

result = data.search(n,k)
if n == 1:
    print(f"<{result[0]}>")
else:
    for i in range(len(result)):
        if i == 0:
            print(f"<{result[i]},",end="")
        elif i == len(result)-1:
            print(f" {result[i]}>")
        else:
            print(f" {result[i]},",end="")

