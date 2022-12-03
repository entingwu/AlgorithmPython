class LinkedNode:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = self.tail.next

    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

    def kick(self, prev):
        curr = prev.next
        if curr == self.tail:
            return
        prev.next = curr.next
        self.key_to_prev[curr.next.key] = prev
        curr.next = None
        self.push_back(curr)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_to_prev:
            return -1

        prev = self.key_to_prev[key]
        curr = prev.next
        self.kick(prev)
        return curr.value


    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.tail.value = value
            return

        self.push_back(LinkedNode(key, value))
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()
