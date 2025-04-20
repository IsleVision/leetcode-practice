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

    // private TreeNode curNode, head;
    private TreeNode tail;

    

    public void flatten(TreeNode root) {
        // if(root==null){
        //     return;
        // }
        // curNode = new TreeNode();
        // head = curNode;
        // preOrd(root);
        // root.left = null;
        // root.right = head.right.right;  

        revPostOrd(root);


    }

    private void revPostOrd(TreeNode root){
        if(root==null){
            return;
        }
        revPostOrd(root.right);
        revPostOrd(root.left);
        root.left=null;
        root.right=tail;
        tail=root;

    }




    // private void preOrd(TreeNode root){
    //     if(root == null){
    //         return;
    //     }
    //     curNode.right = new TreeNode(root.val);
    //     curNode = curNode.right;
    //     preOrd(root.left);
    //     preOrd(root.right);
    // }

}