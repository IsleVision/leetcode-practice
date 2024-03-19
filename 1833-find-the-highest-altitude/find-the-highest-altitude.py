class Solution(object):
    def largestAltitude(self, gain):
        max_al=0
        cur_al=0
        for ga in gain:
            cur_al += ga
            max_al = max(max_al,cur_al)
        return max_al


        