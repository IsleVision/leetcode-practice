class Solution(object):
    def maxVowels(self, s, k):
        vos=['a','e','i','o','u']
        i=0
        max_cnt=0
        cur_cnt=0
        for i in range(k):
            if s[i] in vos:
                cur_cnt+=1
        if cur_cnt == k:
            return k
        max_cnt=cur_cnt    
        for i in range(1,len(s)-k+1,1):
            if s[i-1] in vos:
                cur_cnt -=1
            if s[i+k-1] in vos:
                cur_cnt +=1
            max_cnt = max(max_cnt,cur_cnt)
            if max_cnt == k:
                return k
        return max_cnt
        


        