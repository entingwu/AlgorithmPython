"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Rehashing:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        if not hashTable:
            return []
        H_SIZE = len(hashTable) * 2
        newTable = [None] * H_SIZE

        for head in hashTable:
            while head:
                newKey = head.val % H_SIZE
                if newTable[newKey] is None:
                    newTable[newKey] = ListNode(head.val)
                else:
                    curr = newTable[newKey]
                    while curr.next:
                        curr = curr.next
                    curr.next = ListNode(head.val)
                head = head.next

        return newTable