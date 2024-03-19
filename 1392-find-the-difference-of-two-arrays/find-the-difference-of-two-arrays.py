class Solution(object):
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        com = set1&set2
        return [list(set1-com),list(set2-com)]

        