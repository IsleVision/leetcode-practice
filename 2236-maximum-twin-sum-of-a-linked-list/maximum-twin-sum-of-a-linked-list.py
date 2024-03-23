# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        arr=[head.val]
        tmp = head
        while tmp.next:
            tmp = tmp.next
            arr += [tmp.val]
        length = len(arr)
        max_sum = 0
        for i in range(length/2):
            max_sum = max(max_sum, arr[i]+arr[length-i-1])
        return max_sum




        