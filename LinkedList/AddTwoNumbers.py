from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        bit, carry = 0, 0
        while l1 and l2:
            bit = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            node = ListNode(bit)
            tail.next = node
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            bit = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            tail.next = ListNode(bit)
            tail = tail.next
            l1 = l1.next

        while l2:
            bit = (l2.val + carry) % 10
            carry = (l2.val + carry) / 10
            tail.next = ListNode(bit)
            tail = tail.next
            l2 = l2.next

        if carry == 1:
            tail.next = ListNode(1)
        return dummy.next

if __name__ == '__main__':
    p1 = AddTwoNumbers()
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6
    p1.addTwoNumbers(node1, node4)