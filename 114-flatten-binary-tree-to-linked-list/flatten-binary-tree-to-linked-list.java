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

    private TreeNode curNode, head;
    

    public void flatten(TreeNode root) {
        if(root==null){
            return;
        }
        // TreeNode rightNode = root.right;
        // if(root.left!=null){
        //     root.right=new TreeNode(root.left.val);
        // }

        // flatten(root.left);
        // flatten(rightNode);

        // TreeNode child = new TreeNode();
        curNode = new TreeNode(root.val);
        head = curNode;
        preOrd(root);
        root.left = null;
        root.right = head.right.right;  

    }



    private void preOrd(TreeNode root){
        if(root == null){
            return;
        }
        curNode.right = new TreeNode(root.val);
        curNode = curNode.right;
        preOrd(root.left);
        preOrd(root.right);
    }

}