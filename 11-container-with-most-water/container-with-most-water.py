class Solution(object):
    def maxArea(self, height):
        res = 0
        i,j=0,len(height)-1
        while i<j:
            res = max(res,(j-i)*min(height[i],height[j]))
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return res
