# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        l = []
        cur = deque([root])
        even = False
        while cur:
            n = len(cur)
            now = []
            for i in range(n):
                node = cur.popleft()
                now.append(node.val)
                if node.right:
                    cur.append(node.right)
                if node.left:
                    cur.append(node.left)
            l.append(list(now)) if even else l.append(list(reversed(now)))
            even = not even
        return l
            
        