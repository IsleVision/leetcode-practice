class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        l,r = 0, length-1
        while r-l>1:
            mid = (l+r)//2
            if nums[mid]>=nums[mid-1] and nums[mid]>=nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid-1]:
                r=mid
            else:
                l=mid
        if r-l==0:
            return 0
        else:
            return l if nums[l]>=nums[r] else r



               
        