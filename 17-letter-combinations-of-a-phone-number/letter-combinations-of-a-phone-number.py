class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
        }
        def combine(digits:str, cb:List[str])->List[str]:
            if not digits:
                return cb
            res = []
            if not cb:
                res = list(dic[digits[0]])
            else:
                for x in cb:
                    res += [x+y for y in dic[digits[0]]]
            return combine(digits[1:],res)
        return combine(digits,[])
            


