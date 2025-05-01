class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def add(self,val):
        self.next = ListNode(val)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #what if head.val == head.next.value ?
        if not head or head.next is None:
            return head
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head