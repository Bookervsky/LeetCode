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

// Implemented using deque
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<List<Integer>> l = new ArrayList<>();
        Deque<TreeNode> cur = new ArrayDeque<>();
        cur.add(root);
        while (cur.isEmpty() == false){
            int size = cur.size();
            List<Integer> now = new ArrayList<>(size);
            for (int i = 0; i < size; i++){
                TreeNode node = cur.poll();
                now.add(node.val);
                if (node.left != null) cur.add(node.left);
                if (node.right != null) cur.add(node.right);
            }
            l.add(now);
        }
        return l;
    }
}