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
    private List<String> nums = new LinkedList<>();

    public int sumNumbers(TreeNode root) {
        preOrder(root, root.val+"");
        int res=0;
        for( String num: nums){
            res += Integer.parseInt(num);
        }
        return res;
    }

    public void preOrder(TreeNode root, String acc){
        if(root.left==null&&root.right==null){
            nums.add(acc);
            return;
        }
        if(root.left!=null) preOrder(root.left, acc+root.left.val+"");
        if(root.right!=null) preOrder(root.right, acc+root.right.val+"");
    }


}