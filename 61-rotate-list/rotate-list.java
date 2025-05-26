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
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null||head.next==null){
            return head;
        }


        ListNode tmp = head;
        int length =1;
        while(true){
            length++;
            tmp=tmp.next;
            if( tmp.next==null){
                tmp.next=head;
                break;
            }
        }

        ListNode res=head;

        for(int i=0; i<length-k%length; i++){
            if(i==length-k%length-1){
                tmp=res.next;
                res.next=null;
                res=tmp;
            }
            else{
                res=res.next;
            }
        }

        return res;

    }
}