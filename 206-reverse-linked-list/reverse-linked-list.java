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
    public ListNode reverseList(ListNode head) {
        if(head==null){
            return null;
        }
        else if(head.next==null){
            return head;
        }
        else{
            ListNode headNode = recurReverse(head, head.next);
            head.next = null;
            return headNode;
        }
    }

    public ListNode recurReverse(ListNode head, ListNode next){
        if(next.next==null){
            head.next=null;
            next.next=head;
            return next;
        }
        ListNode headNode = recurReverse(head.next, next.next);
        head.next=null;
        next.next=head;
        return headNode;
    }
}