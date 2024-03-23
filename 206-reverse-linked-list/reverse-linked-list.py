# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        elif not head.next:
            return head
        
        tmp_l=None
        tmp_r=tmp=head
        while tmp.next:
            tmp_r=tmp.next
            tmp.next=tmp_l
            tmp_l=tmp
            tmp = tmp_r
        tmp.next = tmp_l
        return tmp







        