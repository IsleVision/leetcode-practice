class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if k==1:
        #     tmp=nums[0]
        #     for e in nums[1:]:
        #         if e>tmp:
        #             tmp=e
        #     return tmp
        # lgst = self.findKthLargest(nums,1)
        # nums.remove(lgst)
        # return self.findKthLargest(nums,k-1)


        # lgst = []
        # length = len(nums)
        # def wrapper(k: int)->int:
        #     nonlocal lgst
        #     if k==1:
        #         tmp=float(-inf)
        #         tmp_i =0
        #         for i in range(length):
        #             if i not in lgst and nums[i]>tmp:
        #                 tmp=nums[i]
        #                 tmp_i=i
        #         lgst += [tmp_i]
        #         return tmp
        #     wrapper(1)
        #     return wrapper(k-1)
        # return wrapper(k)
        
        # heap = nums[:k]
        # heapq.heapify(heap)
        
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        
        # return heap[0]
        heapq.heapify(nums)
        return heapq.nlargest(k,nums)[-1]


        