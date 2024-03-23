# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        
        tmp_o = head
        tmp = tmp_e = head_e= head.next
        ind_o =True
        while tmp.next:
            tmp = tmp.next
            if ind_o:
                tmp_o.next=tmp
                tmp_o=tmp
            else:
                tmp_e.next=tmp
                tmp_e=tmp
            ind_o = not ind_o
        tmp_o.next=head_e
        tmp_e.next=None
        return head