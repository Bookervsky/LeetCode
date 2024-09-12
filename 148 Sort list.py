class ListNode():
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: # if there is no item or only one item in the list, return the head
            return head
        slow, fast = head, head.next
        # The slow pointer moves one step each time, while the fast pointer moves two steps meanwhile
        # Hence, when the fast pointer reaches the end, the slow poninter is right at the middle of the list
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None # split the list apart and sort list recursively.
        left, right = self.sortList(head), self.sortList(mid) # mid point to the head of the right list

        # merge the two sorted list
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right,right.next
            h = h.next
        h.next = left if left else right
        return res.next