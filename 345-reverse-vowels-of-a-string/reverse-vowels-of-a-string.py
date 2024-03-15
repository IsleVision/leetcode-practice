class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vo = ''
        res = ''
        for w in s:
            if w in vowels:
                vo += w

        for w in s:
            if w in vowels:
                res += vo[-1]
                vo = vo[:-1]    
            else:
                res += w  

        return res            






        