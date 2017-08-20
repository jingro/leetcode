class LRUCache(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = self.prev = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.d = {}
        self.tail = self.head = self.Node(0, 0)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        tNode = self.d[key]
        tNode.prev.next = tNode.next
        if tNode == self.tail:
            self.tail = tNode.prev
        else:
            tNode.next.prev = tNode.prev

        if self.head.next != tNode:
            if not self.head.next:
                self.tail = tNode
            else:
                self.head.next.prev = tNode
            tNode.next = self.head.next
            self.head.next = tNode
            tNode.prev = self.head

        return tNode.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            self.d[key].value = value
            self.get(key)
            return
        if self.size == self.capacity:
            t = self.tail
            self.tail = self.tail.prev
            t.prev.next = None
            t.prev = None
            self.d.pop(t.key)
            self.size -= 1

        tNode = self.Node(key, value)
        if not self.head.next:
            self.tail = tNode
        else:
            self.head.next.prev = tNode
        tNode.next = self.head.next
        self.head.next = tNode
        tNode.prev = self.head
        self.size += 1
        self.d[key] = tNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
