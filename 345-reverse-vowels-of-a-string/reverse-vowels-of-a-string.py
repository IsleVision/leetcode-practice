class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u']
        vo = ''
        res = ''
        for w in s:
            if w.lower() in vowels:
                vo += w

        for w in s:
            if w.lower() in vowels:
                res += vo[-1]
                vo = vo[:-1]    
            else:
                res += w  

        return res            






        