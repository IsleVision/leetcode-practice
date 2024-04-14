class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        length = len(nums1)
        nums = [[i,j] for i,j in zip(nums1,nums2)]
        nums.sort(key=lambda x:x[1],reverse=True)
        heap = [i[0] for i in nums[:k]]
        nums1_sum = sum(heap)
        heapq.heapify(heap)
        max_res = nums1_sum*nums[k-1][1]
        for i in range(k,length): 
            l=heapq.heappop(heap)
            nums1_sum=nums1_sum-l+nums[i][0]   
            tmp = nums1_sum*nums[i][1]
            heapq.heappush(heap,nums[i][0])   
            max_res = max(max_res,tmp)
        return max_res


