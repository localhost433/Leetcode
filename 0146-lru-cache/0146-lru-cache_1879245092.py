class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
      
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def _add_head(self, node: Node) -> None:
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def _move_front(self, node: Node) -> None:
        self._remove(node)
        self._add_head(node)

    def _pop(self) -> Node:
        ret = self.tail.prev
        self._remove(ret)
        return ret

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self._move_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self._move_front(node)
            return
        
        node = Node(key, value)
        self.mp[key] = node
        self._add_head(node)
        
        if len(self.mp) > self.cap:
            d = self._pop()
            del self.mp[d.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)