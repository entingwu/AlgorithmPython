class ImplementQueueByArray:

    def __init__(self):
        self.MAXSIZE = 4
        self.queue = [0] * self.MAXSIZE
        self.head, self.tail = 0, 0

    """
        @param: item: An integer
        @return: nothing
        """

    def enqueue(self, item):
        # queue is full
        if self.tail == self.MAXSIZE:
            return
        self.queue[self.head] = item
        self.tail += 1

    """
    @return: An integer
    """

    def dequeue(self):
        # queue is empty
        if self.head == self.tail:
            return -1

        item = self.queue[self.head]
        self.head += 1
        return item

class Node():
    def __init__(self, _val):
        self.next = None
        self.val_ = _val

class ImplementQueueByLinkedList:

    def __init__(self):
        self.head, self.tail = None, None

    """
            @param: item: An integer
            @return: nothing
            """

    def enqueue(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    """
    @return: An integer
    """

    def dequeue(self):
        if self.head is not None:
            item = self.head.val_
            self.head = self.head.next
            return item
        return -1