# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        arr = [head]
        tmp = head
        while tmp.next:
            tmp = tmp.next
            arr += [tmp]
        length = len(arr)
        if length==1:
            return None
        elif length==2:
            arr[0].next=None
            return head
        else:
            arr[length//2-1].next = arr[length//2+1]
            return head


        