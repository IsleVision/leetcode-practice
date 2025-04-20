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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if(root==null){
            return new LinkedList<>();
        }
        
        List<List<Integer>> res = new LinkedList<>();
        List<List<TreeNode>> resNodes = new LinkedList<>();
        resNodes.add(new LinkedList<>(Arrays.asList(root)));

        boolean rev = false;
        int dep = 0;
        while(true){
            List<TreeNode> curNodes = resNodes.get(dep);
            List<TreeNode> nextNodes = new LinkedList();
            for(int i=0; i<curNodes.size(); i++){
                TreeNode curN = curNodes.get(i);
                if(curN.left!=null){
                    nextNodes.add(curN.left);
                }
                if(curN.right!=null){
                    nextNodes.add(curN.right);
                }
            }
            if(nextNodes.size()!=0){
                resNodes.add(nextNodes);
                dep++;
            }
            else{
                break;
            }
        }

        for(int i=0; i<resNodes.size(); i++){
            List<TreeNode> curNodes = resNodes.get(i);
            List<Integer> nextRes = new LinkedList();
            for(int j=0; j<curNodes.size(); j++){
                if(!rev){
                    nextRes.add(curNodes.get(j).val);
                }
                else{
                    nextRes.add(curNodes.get(curNodes.size()-1-j).val);
                }
            }
            res.add(nextRes);
            rev = !rev;
        }

        return res;
    }
}