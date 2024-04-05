class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # length = len(nums)
        # idx = 0
        # while length>2:
        #     mid = length//2
        #     if nums[mid]>=nums[mid+1] and nums[mid]>=nums[mid-1]:
        #         return idx + mid
        #     elif nums[mid]<nums[mid+1]: 
        #         nums = nums[mid+1:]
        #         idx += mid
        #     else:
        #         nums = nums[0:mid]
        #         idx -=mid
        #     length = len(nums)
        # if length==1:
        #     return
            
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = ((high-low)//2) + low
            # Peak element is present in right side
            if mid < n-1 and nums[mid] < nums[mid+1]:
                low = mid+1
            # Peak element is present in left side
            elif mid > 0 and nums[mid] < nums[mid-1]:
                high = mid-1
            else:
                return mid
            

               
        