class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s:str)->bool:
            length=len(s)
            n=length-1
            while 2*n-length>=0:
                if s[n]!=s[length-1-n]:
                    return False
                n-=1
            return True
        length = len(s)
        for l in range(length,1,-1):
            for i in range(length-l+1):
                if check(s[i:i+l]):
                    return s[i:i+l]
        return s[0]


                