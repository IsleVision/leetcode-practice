class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic_r, dic_m = {},{}
        for e in ransomNote:
            if e not in dic_r:
                dic_r[e]=1
            else:
                dic_r[e] +=1
        for e in magazine:
            if e not in dic_m:
                dic_m[e]=1
            else:
                dic_m[e] +=1
        for k in dic_r:
            if k not in dic_m or dic_r[k]>dic_m[k]:
                return False
        return True
        

        