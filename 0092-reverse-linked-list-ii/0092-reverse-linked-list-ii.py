from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head
        zero = ListNode(0)
        zero.next = head
        cur = zero
        for i in range(right):
            if i == left - 1:
                before = cur
            cur = cur.next
        leftnode = before.next
        after = cur.next
        cur.next = None
        before.next = None
        last = self.reverseList(leftnode)
        before.next = last
        leftnode.next = after
        return zero.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last