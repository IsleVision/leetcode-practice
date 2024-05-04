# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        res=head
        idx =0 
        arr = []
        h,t=None,None
        while head:
            if idx==left-2:
                h=head
            elif idx==right:
                t=head
            elif left-1<=idx<=right-1:
                arr+=[head]
            head=head.next
            idx+=1
        if h:
            h.next=arr[-1]
        if t:
            arr[0].next=t
        else:
            arr[0].next=None
        for i in range(len(arr)-1):
            arr[i+1].next=arr[i]
        return res if h else arr[-1]
        

        