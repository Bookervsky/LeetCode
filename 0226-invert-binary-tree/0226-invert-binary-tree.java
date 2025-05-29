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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        return sub(root);
    }
    public TreeNode sub(TreeNode root){
        if (root == null) return null;
        if (root.left == null && root.right == null) return root;
        TreeNode tmp = root.left;
        root.left = sub(root.right);
        root.right = sub(tmp);
        return root;
    }
}