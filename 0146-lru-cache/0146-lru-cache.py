class Node():
    def __init__(self, data, key):
        self.data = data
        self.prev = None
        self.next = None
        self.key = key

class DoublyLinkedList():
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.count = 0
        self.capacity = capacity
        self.key_dict = {}

    def get_data(self, key):
        if key not in self.key_dict:
            return -1
        
        cur_data = self.key_dict[key]
        if cur_data == self.head : return cur_data.data
        if cur_data.next == None:
            cur_data.prev.next = None
            self.tail = cur_data.prev  
        else:
            cur_data.next.prev = cur_data.prev
            cur_data.prev.next = cur_data.next

        cur_data.next = self.head
        cur_data.prev = None

        self.head.prev = cur_data
        self.head = cur_data

        return cur_data.data


    def append_head(self, key, data):
        if key in self.key_dict:
            node = self.key_dict[key]
            node.data = data
            self.get_data(key)
            return

        new_data = Node(data, key)
        self.key_dict[key] = new_data
        if self.count == self.capacity :
            self.pop_tail()
            #self.count -= 1 -> 이거 회고에 적어야겠다

        if self.count == 0:
            self.head = new_data
            self.tail = new_data
            self.count += 1
        else:
            new_data.next = self.head
            self.head.prev = new_data
            
            self.head = new_data

            self.count += 1

    def pop_tail(self):
        if self.count == 0:
            return None

        node = self.tail

        del self.key_dict[node.key]

        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        node.next = None
        node.prev = None

        self.count -= 1


class LRUCache:
    def __init__(self, capacity: int):
        self.dblist = DoublyLinkedList(capacity = capacity)

    def get(self, key: int) -> int:
        result = self.dblist.get_data(key = key)
        return result

    def put(self, key: int, value: int) -> None:
        self.dblist.append_head(key = key, data = value)