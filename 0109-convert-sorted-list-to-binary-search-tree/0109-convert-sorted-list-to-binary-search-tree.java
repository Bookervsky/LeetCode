/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        ListNode p = head;
        while (p.next != null){
            p = p.next;
        }
        TreeNode root = help(head, null);
        return root;
    }

    public TreeNode help(ListNode left, ListNode right){
        if (left == right) return null;
        ListNode mid = findmid(left);
        ListNode tmp = mid.next;
        mid.next = null;
        TreeNode root = new TreeNode(mid.val);
        root.left = help(left, mid);
        root.right = help(tmp, right);
        return root;
    }

    public ListNode findmid(ListNode head){
        if (head.next == null) return head;
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}