# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        arr = [head]
        rm = False
        while head.next:
            if head.val==head.next.val and rm==False:
                arr.pop()
                rm=True
            elif head.val!=head.next.val:
                arr +=[head.next]
                rm = False
            head=head.next
        if not arr:
            return
        for i in range(len(arr)-1):
            arr[i].next=arr[i+1]
        arr[-1].next=None
        return arr[0]


        